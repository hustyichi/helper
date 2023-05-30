import requests
from bs4 import BeautifulSoup

session = requests.Session()


def get_response(
    url: str, timeout: int = 10
):
    try:
        response = session.get(url, timeout=timeout)

        # Check if the response contains an HTTP error
        if response.status_code >= 400:
            return None, f"Error: HTTP {str(response.status_code)} error"

        return response, None
    except ValueError as ve:
        # Handle invalid URL format
        return None, f"Error: {str(ve)}"

    except requests.exceptions.RequestException as re:
        # Handle exceptions related to the HTTP request
        #  (e.g., connection errors, timeouts, etc.)
        return None, f"Error: {str(re)}"


def scrape_text(url: str) -> str:
    response, error_message = get_response(url)
    if error_message:
        return error_message
    if not response:
        return "Error: Could not get response"

    soup = BeautifulSoup(response.text, "html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = "\n".join(chunk for chunk in chunks if chunk)

    return text
