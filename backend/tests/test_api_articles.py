from fastapi.testclient import TestClient

from app.main import app
from app.db.session import SessionLocal, engine
from app.db import models


client = TestClient(app)


def setup_module() -> None:
    models.Base.metadata.create_all(bind=engine)


def test_health() -> None:
    r = client.get("/healthz")
    assert r.status_code == 200


def test_create_and_get_articles() -> None:
    db = SessionLocal()
    source = models.Source(type="rss", name="Test", url="http://example.com")
    db.add(source)
    article = models.Article(
        source=source, url="http://example.com/1", title="Hello", content="Body"
    )
    db.add(article)
    db.commit()
    db.close()

    r = client.get("/articles")
    assert r.status_code == 200
    assert r.json()[0]["title"] == "Hello"
