import requests
from .adapter_base import Summarizer
from app.core.config import get_settings


class OllamaSummarizer(Summarizer):
    def __init__(self, model: str = "mistral") -> None:
        self.model = model
        self.base_url = get_settings().ollama_base_url

    def summarize(self, text: str) -> str:
        payload = {"model": self.model, "prompt": f"Summarize:\n{text}"}
        try:
            r = requests.post(f"{self.base_url}/api/generate", json=payload, timeout=30)
            if r.ok:
                data = r.json()
                return data.get("response", "")[:500]
        except Exception:
            pass
        return text[:200]
