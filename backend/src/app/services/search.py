from typing import List
from sqlalchemy.orm import Session
from app.db import models


def keyword_search(db: Session, query: str) -> List[models.Article]:
    return db.query(models.Article).filter(models.Article.title.ilike(f"%{query}%")).all()
