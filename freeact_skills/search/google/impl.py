import os

from google import genai
from google.genai.types import GenerateContentConfig, GoogleSearch, Tool

SEARCH = Tool(google_search=GoogleSearch())
CONFIG = {
    "model": "gemini-2.0-flash-exp",
    "config": GenerateContentConfig(
        temperature=0.0,
        tools=[SEARCH],
    ),
}


def client(api_key: str | None = None):
    return genai.Client(
        api_key=api_key or os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"),
        http_options={"api_version": "v1alpha"},
    )


def search(query: str, api_key: str | None = None):
    return client(api_key).models.generate_content(contents=query, **CONFIG).text


def search_stream(query: str, api_key: str | None = None):
    for chunk in client(api_key).models.generate_content_stream(contents=query, **CONFIG):
        yield chunk.text
