import json
from itertools import islice

from duckduckgo_search import DDGS


def safe_google_results(results) -> str:
    if isinstance(results, list):
        safe_message = json.dumps(
            [result.encode("utf-8", "ignore").decode("utf-8") for result in results]
        )
    else:
        safe_message = results.encode("utf-8", "ignore").decode("utf-8")
    return safe_message


def duckduckgo_search(query: str, num_results: int = 8) -> str:
    search_results = []
    if not query:
        return json.dumps(search_results)

    results = DDGS().text(query)
    if not results:
        return json.dumps(search_results)

    for item in islice(results, num_results):
        search_results.append(item)

    return search_results
