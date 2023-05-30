import os

from helper.singleton import Singleton


class Config(metaclass=Singleton):
    def __init__(self) -> None:
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

    def set_openai_api_key(self, value: str) -> None:
        """Set the OpenAI API key value."""
        self.openai_api_key = value
