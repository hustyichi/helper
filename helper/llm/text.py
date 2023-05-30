from typing import Optional

import logging

from helper.config import Config
from helper.llm.api_manager import ApiManager

CFG = Config()

logger = logging.getLogger(__name__)


def summarize_text(
    text: str, question: Optional[str] = None
):
    if not text:
        raise ValueError("No text to summarize")

    instruction = None
    if question:
        instruction = (
            f'include any information that can be used to answer the question "{question}". '
            "Do not directly answer the question itself"
        )

    prompt = f"""
        Write a concise of the following text summary
        {'; {instruction}' if instruction is not None else ''}:
        "\n\n\n"
        LITERAL TEXT: ```{text}```
        "\n\n\n"
        "CONCISE SUMMARY: The text is best summarized as"
    """

    messages = [
        {
            "role": "user", "content": prompt
        }
    ]

    api_manager = ApiManager()
    summary = api_manager.create_chat_completion(messages, "gpt-3.5-turbo", temperature=0, max_tokens=500)

    return summary.strip()
