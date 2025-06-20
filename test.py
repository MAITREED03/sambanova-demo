from openai import AsyncOpenAI
import asyncio
import os 
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def main():
    async with AsyncOpenAI(
        base_url="https://api.sambanova.ai/v1", 
        api_key=os.getenv("SAMBANOVA_API_KEY")
    ) as client:
        completion = await client.chat.completions.create(
            model="Meta-Llama-3.1-8B-Instruct",
            messages = [
                {"role": "system", "content": "Answer the question in a couple sentences."},
                {"role": "user", "content": "Share a happy story with me"}
            ]
        )
        print(completion.choices[0].message.content)

if __name__ == "__main__":
    asyncio.run(main())