"""
NVIDIA NIM client wrapper.

Used for the quality-critical interactive tool (Section 4).
The model is configured via NVIDIA_GENERATOR in config.py.
"""

import logging
from typing import Optional

from src.config import NVIDIA_GENERATOR
from src.api.client import get_client

logger = logging.getLogger(__name__)


async def generate_poem_nvidia(
    messages: list[dict[str, str]],
    temperature: float = 1.0,
    max_tokens: Optional[int] = None,
) -> tuple[str, str, dict]:
    """
    Generate a poem using the NVIDIA-hosted generator model.

    Returns:
        (content, served_model_id, usage_dict)
    """
    client = get_client(NVIDIA_GENERATOR)

    response = await client.chat_completion(
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    content = client.get_content(response)
    served_model = client.get_served_model(response)
    usage = client.get_usage(response)
    return content, served_model, usage
