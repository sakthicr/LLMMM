"""
Async HTTP client with ACCOUNT-LEVEL rate limiting, per-model token tracking,
exponential backoff with jitter, and response-model logging.

KEY DESIGN:
  GPT-OSS-120B and Qwen3.8-27B share the same Groq API key and the same
  30 RPM account-wide ceiling.  A shared AccountRateLimiter, keyed by
  (endpoint, api_key_env), enforces a single 25 RPM rolling window
  (5 RPM headroom below the hard cap).  Every outgoing request — regardless
  of which model client sends it — must acquire a slot from this shared
  limiter BEFORE the HTTP call fires.

  Per-model counters still exist for daily tracking and logging.
"""

import asyncio
import json
import random
import time
import logging
from dataclasses import dataclass, field
from typing import Any, Optional

import httpx

from src.config import ModelConfig

logger = logging.getLogger(__name__)


# ── Shared account-level rate limiter ────────────────────────────────────────

class AccountRateLimiter:
    """
    Paces outgoing requests across ALL models sharing the same
    (endpoint, api_key_env) — i.e. the same Groq account.

    Uses a rolling 60-second window capped at `max_rpm` requests.
    Requests call `acquire()` and block until a slot is available.
    """

    def __init__(self, max_rpm: int = 25, max_tpm: int = 6000):
        self.max_rpm = max_rpm
        self.max_tpm = max_tpm
        self._requests: list[float] = []
        self._tokens: list[tuple[float, int]] = []
        self._lock = asyncio.Lock()

    def _prune(self):
        cutoff = time.time() - 60
        self._requests = [t for t in self._requests if t > cutoff]
        self._tokens = [(t, n) for (t, n) in self._tokens if t > cutoff]

    async def acquire(self, estimated_tokens: int, label: str = ""):
        """Block until we can send one more request and fit estimated_tokens."""
        while True:
            async with self._lock:
                self._prune()
                current_tokens = sum(n for (_, n) in self._tokens)
                
                # Check if both RPM and TPM slots are available
                if len(self._requests) < self.max_rpm and (current_tokens + estimated_tokens) <= self.max_tpm:
                    now = time.time()
                    self._requests.append(now)
                    self._tokens.append((now, estimated_tokens))
                    return  # slot acquired

                # Need to wait — compute how long until the oldest slot (RPM or TPM) expires
                wait_time = 0.5
                if len(self._requests) >= self.max_rpm:
                    wait_time = max(wait_time, 60 - (time.time() - self._requests[0]) + 0.5)
                if (current_tokens + estimated_tokens) > self.max_tpm:
                    # Find how many tokens we need to free up
                    needed = (current_tokens + estimated_tokens) - self.max_tpm
                    freed = 0
                    for t, n in self._tokens:
                        freed += n
                        if freed >= needed:
                            wait_time = max(wait_time, 60 - (time.time() - t) + 0.5)
                            break
                            
            if wait_time > 0:
                logger.info(
                    f"[Account Limiter] RPM={len(self._requests)}/{self.max_rpm} "
                    f"TPM={current_tokens}/{self.max_tpm}, waiting {wait_time:.1f}s "
                    f"({label})"
                )
                await asyncio.sleep(wait_time)


# Registry of account-level limiters, keyed by (endpoint, api_key_env)
_account_limiters: dict[tuple[str, str], AccountRateLimiter] = {}

# The Groq free-tier hard cap is 30 RPM; we target 25 to leave headroom.
_GROQ_SAFE_RPM = 25


def _get_account_limiter(config: ModelConfig) -> AccountRateLimiter:
    """Get or create a shared account-level rate limiter."""
    key = (config.endpoint, config.api_key_env)
    if key not in _account_limiters:
        _account_limiters[key] = AccountRateLimiter(max_rpm=_GROQ_SAFE_RPM)
    return _account_limiters[key]


# ── Per-model usage stats ────────────────────────────────────────────────────

@dataclass
class UsageStats:
    """Tracks cumulative usage for one model."""
    requests_today: int = 0
    tokens_today: int = 0
    prompt_tokens_today: int = 0
    completion_tokens_today: int = 0
    requests_this_minute: list = field(default_factory=list)  # timestamps
    tokens_this_minute: list = field(default_factory=list)    # (timestamp, token_count)
    in_flight_tokens: int = 0
    day_start: float = field(default_factory=time.time)

    def reset_if_new_day(self):
        now = time.time()
        if now - self.day_start > 86400:
            self.requests_today = 0
            self.tokens_today = 0
            self.prompt_tokens_today = 0
            self.completion_tokens_today = 0
            self.day_start = now

    def prune_minute_window(self):
        cutoff = time.time() - 60
        self.requests_this_minute = [
            t for t in self.requests_this_minute if t > cutoff
        ]
        self.tokens_this_minute = [
            (t, n) for t, n in self.tokens_this_minute if t > cutoff
        ]

    def tokens_in_last_minute(self) -> int:
        """Sum of tokens consumed in the last 60 seconds."""
        self.prune_minute_window()
        return sum(n for _, n in self.tokens_this_minute)


class RateLimitedClient:
    """
    Async OpenAI-compatible chat completion client with:
    - Shared account-level RPM limiter (gates calls BEFORE sending)
    - Per-model daily request and token counters
    - Exponential backoff with jitter on 429/5xx
    - Response model field logging
    """

    def __init__(self, model_config: ModelConfig, timeout: float = 120.0):
        self.config = model_config
        self.usage = UsageStats()
        self._lock = asyncio.Lock()
        self._account_limiter = _get_account_limiter(model_config)
        self._client = httpx.AsyncClient(
            base_url=model_config.endpoint,
            headers={
                "Authorization": f"Bearer {model_config.api_key}",
                "Content-Type": "application/json",
            },
            timeout=httpx.Timeout(timeout, connect=30.0),
        )

    async def close(self):
        await self._client.aclose()

    async def _check_daily_limits(self, estimated_tokens: int = 0):
        """Check daily RPD and TPD limits (per-model). Raise if exceeded."""
        self.usage.reset_if_new_day()

        # Check daily request limit
        if self.usage.requests_today >= self.config.rpd:
            logger.warning(
                f"[{self.config.name}] Daily request limit ({self.config.rpd}) reached. "
                f"Cannot make more requests today."
            )
            raise RuntimeError(
                f"Daily request limit reached for {self.config.name}"
            )

        # Check daily token limit (with 85% safety margin)
        tpd_limit = self.config.tpd * 0.85
        if self.usage.tokens_today + estimated_tokens >= tpd_limit:
            logger.warning(
                f"[{self.config.name}] Daily token limit ({self.config.tpd}) reached."
            )
            raise RuntimeError(
                f"Daily token limit reached for {self.config.name}"
            )

    async def chat_completion(
        self,
        messages: list[dict[str, str]],
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        retries: int = 50,
    ) -> dict[str, Any]:
        """
        Send a chat completion request with rate limiting and retries.

        Flow:
        1. Check daily limits (per-model)
        2. Acquire a slot from the SHARED account-level RPM limiter
        3. Send the request
        4. On 429/5xx: back off AND re-acquire a slot before retrying
        """
        if max_tokens is None:
            max_tokens = self.config.max_output_tokens

        # Estimate token cost
        estimated_prompt_tokens = sum(len(m.get("content", "")) for m in messages) // 4
        estimated_total_tokens = estimated_prompt_tokens + max_tokens

        payload = {
            "model": self.config.model_id,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        if "gpt-oss" in self.config.model_id:
            payload["reasoning_effort"] = "low"

        for attempt in range(retries):
            # 1. Check daily limits
            await self._check_daily_limits(estimated_total_tokens)

            # 2. Acquire slot from the shared account-level limiter
            #    This ensures we respect both RPM and TPM across all requests.
            await self._account_limiter.acquire(estimated_tokens=estimated_total_tokens, label=self.config.name)

            # 3. Track per-model stats
            async with self._lock:
                self.usage.requests_this_minute.append(time.time())
                self.usage.requests_today += 1

            try:
                response = await self._client.post(
                    "/chat/completions",
                    json=payload,
                )

                if response.status_code == 429:
                    wait = self._backoff_time(attempt)
                    
                    # Try to extract the retry-after or error message
                    err_msg = ""
                    try:
                        err_json = response.json()
                        err_msg = err_json.get("error", {}).get("message", "")
                        
                        # Try to parse exact wait time from Groq's message:
                        # e.g., "Please try again in 4m38.208s." or "Please try again in 45.36s."
                        import re
                        match = re.search(r"Please try again in (?:(\d+)m)?([\d\.]+)s", err_msg)
                        if match:
                            mins = int(match.group(1)) if match.group(1) else 0
                            secs = float(match.group(2))
                            wait = mins * 60 + secs + 1.0  # add 1s buffer
                        elif response.headers.get("retry-after"):
                            wait = float(response.headers.get("retry-after")) + 1.0
                    except Exception:
                        err_msg = response.text[:200]
                        
                    logger.warning(
                        f"[{self.config.name}] Rate limited (429), msg='{err_msg}', "
                        f"retrying in {wait:.1f}s (attempt {attempt+1}/{retries})"
                    )
                    await asyncio.sleep(wait)
                    continue

                if response.status_code >= 500:
                    wait = self._backoff_time(attempt)
                    logger.warning(
                        f"[{self.config.name}] Server error ({response.status_code}), "
                        f"retrying in {wait:.1f}s (attempt {attempt+1}/{retries})"
                    )
                    await asyncio.sleep(wait)
                    continue

                response.raise_for_status()
                data = response.json()

                # Track token usage
                usage = data.get("usage", {})
                total_tokens = usage.get("total_tokens", 0)
                prompt_tokens = usage.get("prompt_tokens", 0)
                completion_tokens = usage.get("completion_tokens", 0)

                async with self._lock:
                    self.usage.tokens_today += total_tokens
                    self.usage.prompt_tokens_today += prompt_tokens
                    self.usage.completion_tokens_today += completion_tokens
                    # Record tokens in the sliding minute window for TPM
                    self.usage.tokens_this_minute.append((time.time(), total_tokens))

                # Log the actual model served
                served_model = data.get("model", "unknown")
                if served_model != self.config.model_id:
                    logger.info(
                        f"[{self.config.name}] Requested '{self.config.model_id}', "
                        f"served '{served_model}'"
                    )

                logger.info(
                    f"[{self.config.name}] Call complete: {prompt_tokens} prompt + "
                    f"{completion_tokens} completion tokens "
                    f"(day total: {self.usage.tokens_today}/{self.config.tpd})"
                )

                return data

            except (httpx.TimeoutException, httpx.ReadError, httpx.ConnectError):
                wait = self._backoff_time(attempt)
                logger.warning(
                    f"[{self.config.name}] Timeout/Connection Error, retrying in {wait:.1f}s "
                    f"(attempt {attempt+1}/{retries})"
                )
                await asyncio.sleep(wait)
            except httpx.HTTPStatusError as e:
                if attempt < retries - 1:
                    wait = self._backoff_time(attempt)
                    logger.warning(
                        f"[{self.config.name}] HTTP {e.response.status_code}, {e.response.text}, "
                        f"retrying in {wait:.1f}s"
                    )
                    await asyncio.sleep(wait)
                else:
                    raise

        raise RuntimeError(
            f"[{self.config.name}] All {retries} attempts failed"
        )

    def _backoff_time(self, attempt: int) -> float:
        """Exponential backoff with jitter."""
        base = min(2 ** attempt, 60)
        jitter = random.uniform(0, base * 0.5)
        return base + jitter

    def get_content(self, response: dict) -> str:
        """Extract the text content from a chat completion response."""
        choices = response.get("choices", [])
        if not choices:
            raise ValueError("Empty choices in API response")
        return choices[0]["message"]["content"]

    def get_served_model(self, response: dict) -> str:
        """Extract the actual model ID served by the API."""
        return response.get("model", "unknown")

    def get_usage(self, response: dict) -> dict:
        """Extract token usage from a response."""
        return response.get("usage", {})

    @property
    def daily_usage_summary(self) -> str:
        self.usage.reset_if_new_day()
        return (
            f"[{self.config.name}] "
            f"Requests: {self.usage.requests_today}/{self.config.rpd} | "
            f"Tokens: {self.usage.tokens_today}/{self.config.tpd} "
            f"(prompt={self.usage.prompt_tokens_today}, "
            f"completion={self.usage.completion_tokens_today})"
        )


# ── Singleton client registry ────────────────────────────────────────────────

_clients: dict[str, RateLimitedClient] = {}


def get_client(model_config: ModelConfig) -> RateLimitedClient:
    """Get or create a rate-limited client for the given model config."""
    key = f"{model_config.endpoint}:{model_config.model_id}"
    if key not in _clients:
        _clients[key] = RateLimitedClient(model_config)
    return _clients[key]


async def close_all_clients():
    """Cleanup: close all open HTTP clients."""
    for client in _clients.values():
        await client.close()
    _clients.clear()
