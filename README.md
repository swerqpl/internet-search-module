# Internet Search & Summarization Module

This Python module allows your app to:
- Detect if a user's question requires an internet search.
- Use **DuckDuckGo** to search the web.
- Select the most relevant results using a language model (OpenAI API).
- Extract and summarize content from selected web pages.

## Features

- Works with Polish-language user questions.
- Uses DuckDuckGo (no API key needed).
- Filters links using OpenAI (e.g., GPT-4 or GPT-3.5).
- Summarizes web content to directly answer user intent.

## Requirements

Install dependencies:

```bash
pip install openai requests beautifulsoup4 trafilatura python-dotenv
```

Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your-api-key-here
```

## Usage

Use the `search_and_summarize()` function and pass a question in Polish. It will return a string summary or `None`.

Example:

```python
from search_module import search_and_summarize

result = search_and_summarize("Jakie są najnowsze wiadomości ze świata technologii?")
print(result)
```

## Notes

- Internet access and a valid OpenAI API key are required.
- Uses DuckDuckGo for web search (no tracking, no account required).
- Summarization uses OpenAI models (`gpt-4`, `gpt-3.5-turbo`, etc.).
- Beware of API token limits and usage costs.

## Contributing

Pull requests and ideas are welcome!
