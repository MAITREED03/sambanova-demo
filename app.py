import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.sambanova.ai/v1",
    api_key=os.getenv("SAMBANOVA_API_KEY")
)

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "Answer the question in a couple sentences."},
        {"role": "user", "content": "Share a happy story with me"}
    ],
    model="Meta-Llama-3.1-405B-Instruct"
)

print(chat_completion.choices[0].message.content)