import asyncio
from src.config import GPT_OSS_120B
from src.api.groq_client import generate_poem_groq

async def test_capacity():
    messages = [{"role": "user", "content": "Hello"}]
    try:
        content, model, usage = await generate_poem_groq(messages, max_tokens=10)
        print("SUCCESS:", content)
    except Exception as e:
        print("ERROR:", str(e))

if __name__ == "__main__":
    asyncio.run(test_capacity())
