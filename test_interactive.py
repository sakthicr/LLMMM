import asyncio
import sys
import logging
from unittest.mock import patch

# Fix Windows console encoding — cp1252 cannot handle Unicode symbols
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from rich.prompt import Prompt, IntPrompt

from src.interactive.tool import run_interactive_tool
from src.api.client import close_all_clients

prompt_answers = [
    "A programmer fixing bugs",
    "bad",
    "good",
    "no"
]

def mock_prompt_ask(question, *args, **kwargs):
    if "description" in question.lower():
        ans = "A programmer fixing bugs"
    elif "good?" in question.lower():
        if mock_prompt_ask.good_calls == 0:
            ans = "bad"
            mock_prompt_ask.good_calls += 1
        else:
            ans = "good"
    elif "another" in question.lower():
        ans = "no"
    else:
        ans = prompt_answers.pop(0)
    print(f"Mocked Prompt.ask('{question}') -> {ans}")
    return ans

mock_prompt_ask.good_calls = 0

def mock_intprompt_ask(question, *args, **kwargs):
    if "poem type" in question.lower():
        ans = 2
    elif "algorithm" in question.lower():
        ans = 2
    elif "emotion" in question.lower():
        ans = 1
    else:
        ans = 1
    print(f"Mocked IntPrompt.ask('{question}') -> {ans}")
    return ans

async def main():
    with patch("src.interactive.tool.Prompt.ask", side_effect=mock_prompt_ask):
        with patch("src.interactive.tool.IntPrompt.ask", side_effect=mock_intprompt_ask):
            try:
                await run_interactive_tool()
            finally:
                await close_all_clients()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
