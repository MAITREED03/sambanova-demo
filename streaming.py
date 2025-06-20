from openai import OpenAI
from openai import AsyncOpenAI
import asyncio
import os 
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = OpenAI(
    base_url="https://api.sambanova.ai/v1", 
    api_key= os.getenv("SAMBANOVA_API_KEY")
)
completion = client.chat.completions.create(
    model="Meta-Llama-3.1-8B-Instruct",
    messages = [
        {"role": "system", "content": "Answer the question in a couple sentences."},
        {"role": "user", "content": "Share a happy story with me"}
    ],
    stream = True
)
for chunk in completion:
  print(chunk.choices[0].delta.content, end="")