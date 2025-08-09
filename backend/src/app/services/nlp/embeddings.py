from typing import List
from sqlalchemy import text
from sqlalchemy.orm import Session


EMBEDDING_DIM = 384


def embed_text(text: str) -> List[float]:
    return [0.0] * EMBEDDING_DIM


def store_embedding(db: Session, article_id: int, emb: List[float]) -> None:
    db.execute(
        text("UPDATE articles SET embedding = :emb WHERE id=:id"),
        {"emb": emb, "id": article_id},
    )
    db.commit()
