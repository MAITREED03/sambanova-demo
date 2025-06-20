import openai
import cmath
import json
import os
import random
from dotenv import load_dotenv

load_dotenv()

# Initialize the client with SN Cloud base URL and your API key
client = openai.OpenAI(
    base_url="https://api.sambanova.ai/v1",
    api_key=os.getenv("SAMBANOVA_API_KEY")
)

response = client.embeddings.create(
    model="E5-Mistral-7B-Instruct",
    input=[
        "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
        "Jupiter's Great Red Spot is a storm that has been raging for at least 350 years."
    ]
)

print(response)