from app.services.ingest import rss_ingestor
from app.services.ingest.normalizer import normalize_article
from app.db import models
from app.db.session import SessionLocal


def poll_rss(url: str) -> None:
    items = rss_ingestor.fetch_rss(url)
    db = SessionLocal()
    for item in items:
        norm = normalize_article({"url": item["link"], "title": item["title"], "content": ""})
        article = models.Article(
            source_id=1, url=norm["canonical_url"], title=item["title"], content=""
        )
        db.add(article)
    db.commit()
    db.close()
