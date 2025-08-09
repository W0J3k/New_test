from transformers import pipeline
from .adapter_base import Summarizer


class HFSummarizer(Summarizer):
    def __init__(self, model: str = "sshleifer/distilbart-cnn-12-6") -> None:
        self.pipeline = pipeline("summarization", model=model)

    def summarize(self, text: str) -> str:
        try:
            return self.pipeline(text)[0]["summary_text"]
        except Exception:
            return text[:200]
