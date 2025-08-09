from app.services.nlp.summarizer import get_default_summarizer


def test_summarizer_basic() -> None:
    summarizer = get_default_summarizer()
    text = "Sentence one. Sentence two. " * 5
    summary = summarizer.summarize(text)
    assert isinstance(summary, str)
    assert len(summary) > 0
