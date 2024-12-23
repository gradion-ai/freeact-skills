class InternetSearch:
    """Search for up-to-date information on the internet"""

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key

    def search(self, natural_language_query: str):
        """
        Search for up-to-date information on the internet and stream the result to stdout in markdown format.

        Args:
            natural_language_query (str): A query string that matches a specific topic, concept, or fact.
              It should be formulated in natural language and be as specific as possible.
        """
        from freeact_skills.search.google import impl

        for chunk in impl.search_stream(natural_language_query, self.api_key):
            print(chunk, end="", flush=True)
