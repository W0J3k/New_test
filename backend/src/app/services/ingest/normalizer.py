from urllib.parse import urlparse
from langdetect import detect
from app.utils.simhash import simhash


def canonical_url(url: str) -> str:
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"


def normalize_article(article: dict) -> dict:
    article["canonical_url"] = canonical_url(article.get("url", ""))
    content = article.get("content", "")
    try:
        article["language"] = detect(content[:200]) if content else "unknown"
    except Exception:
        article["language"] = "unknown"
    article["content_hash"] = simhash(content)
    return article
