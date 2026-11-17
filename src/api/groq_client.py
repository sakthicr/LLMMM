"""
Groq client wrapper for GPT-OSS-120B (bulk generator) and Qwen3.8-27B (judge).

Both models share the same API key but have independent rate limiters
(different ModelConfig instances → different RateLimitedClient instances).
"""

import logging
from typing import Optional

from src.config import GPT_OSS_120B, QWEN_27B
from src.api.client import get_client

logger = logging.getLogger(__name__)


async def generate_poem_groq(
    messages: list[dict[str, str]],
    temperature: float = 0.8,
    max_tokens: Optional[int] = None,
) -> tuple[str, str, dict]:
    """
    Generate a poem using GPT-OSS-120B via Groq.

    Used for the bulk statistical grid (Section 8).

    Returns:
        (content, served_model_id, usage_dict)
    """
    client = get_client(GPT_OSS_120B)
    response = await client.chat_completion(
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    content = client.get_content(response)
    served_model = client.get_served_model(response)
    usage = client.get_usage(response)
    return content, served_model, usage


async def judge_poem_groq(
    messages: list[dict[str, str]],
    temperature: float = 0.0,
    max_tokens: Optional[int] = 512,
) -> tuple[str, str, dict]:
    """
    Score a poem using Qwen3.8-27B via Groq (the Judge model).

    Lower temperature for more consistent scoring.

    Returns:
        (content, served_model_id, usage_dict)
    """
    client = get_client(QWEN_27B)
    response = await client.chat_completion(
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    content = client.get_content(response)
    served_model = client.get_served_model(response)
    usage = client.get_usage(response)
    return content, served_model, usage
