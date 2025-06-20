import openai
import cmath
import json
import os
import random
from dotenv import load_dotenv

# Initialize the client with SN Cloud base URL and your API key
client = openai.OpenAI(
    base_url="https://api.sambanova.ai/v1", 
    api_key= os.getenv("SAMBANOVA_API_KEY")
)

MODEL = "Meta-Llama-3.1-8B-Instruct"
def get_weather(city: str) -> dict:
    """
    Fake weather lookup: returns a random temperature between 20°C and 50°C.
    """
    temp = random.randint(20, 50)
    return {
        "city": city,
        "temperature_celsius": temp
    }

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of an location, the user shoud supply a location first",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["city"]
            },
        }
    },
]

messages = [{"role": "user", "content": "What's the weather like in Paris today?"}]


completion = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    tools=tools
)

# Print the actual response content
response_message = completion.choices[0].message
print("\nAssistant's response:")
print(response_message.content)

# If there are tool calls, print those as well
if response_message.tool_calls:
    print("\nTool calls:")
    for tool_call in response_message.tool_calls:
        if tool_call.function.name == "get_weather":
            function_args = json.loads(tool_call.function.arguments)
            weather_result = get_weather(function_args["city"])
            print(f"Weather for {function_args['city']}: {weather_result}")