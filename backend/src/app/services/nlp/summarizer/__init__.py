from .adapter_base import Summarizer
from .ollama_adapter import OllamaSummarizer


def get_default_summarizer() -> Summarizer:
    return OllamaSummarizer()
