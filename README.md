# SambaNova Function Calling Demo

This project demonstrates how to use the SambaNova API with OpenAI-compatible clients to perform function calling, such as retrieving weather information for a given city.

## Features

- Uses the SambaNova API with OpenAI's Python client
- Demonstrates function calling with a fake weather lookup
- Shows how to structure tool/function schemas for LLMs

## Requirements

- Python 3.8+
- `openai` Python package
- `python-dotenv` package (for loading environment variables)
- SambaNova API key

## Setup

1. **Clone the repository**  
   ```sh
   git clone <your-repo-url>
   cd sambanova
   ```

2. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your environment variables**  
   Create a `.env` file in the project root:
   ```
   SAMBANOVA_API_KEY=your-api-key-here
   ```

## Usage

Run any of the example scripts:

```sh
python app.py
python test.py
python functioncalling.py
python jsonschema.py
```

Each script demonstrates a different aspect of interacting with the SambaNova API.

## Example Output

```
Assistant's response:
The weather in Paris today is 32°C and sunny.

Tool calls:
Weather for Paris: {'city': 'Paris', 'temperature_celsius': 32}
```

## Notes

- The weather function is a mock and returns random temperatures.
- Make sure your API key is valid and has access to the specified model.
- Update the model name in the scripts if SambaNova releases new models.

## License

MIT License
