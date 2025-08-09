import openai
from .adapter_base import Summarizer
from app.core.config import get_settings


class OpenAISummarizer(Summarizer):
    def __init__(self, model: str = "gpt-3.5-turbo") -> None:
        openai.api_key = get_settings().openai_api_key
        self.model = model

    def summarize(self, text: str) -> str:
        try:
            resp = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": f"Summarize:\n{text}"}],
            )
            return resp.choices[0].message["content"]  # type: ignore[index]
        except Exception:
            return text[:200]
