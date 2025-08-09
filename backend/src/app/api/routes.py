from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db_session
from app.db import models, schemas
from app.services.nlp.summarizer import get_default_summarizer

router = APIRouter()


@router.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/sources", response_model=schemas.SourceRead)
def create_source(
    source: schemas.SourceCreate, db: Session = Depends(get_db_session)
) -> models.Source:
    db_source = models.Source(**source.dict())
    db.add(db_source)
    db.commit()
    db.refresh(db_source)
    return db_source


@router.get("/articles", response_model=List[schemas.ArticleRead])
def list_articles(
    source_id: int | None = None, db: Session = Depends(get_db_session)
) -> List[models.Article]:
    q = db.query(models.Article)
    if source_id:
        q = q.filter(models.Article.source_id == source_id)
    return q.all()


@router.get("/articles/{article_id}", response_model=schemas.ArticleRead)
def get_article(article_id: int, db: Session = Depends(get_db_session)) -> models.Article:
    article = db.get(models.Article, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@router.post("/summarize")
def summarize(
    req: schemas.SummarizeRequest, db: Session = Depends(get_db_session)
) -> dict[str, str]:
    summarizer = get_default_summarizer()
    texts: List[str] = []
    if req.ids:
        articles = db.query(models.Article).filter(models.Article.id.in_(req.ids)).all()
        texts = [a.content for a in articles]
    elif req.query:
        articles = db.query(models.Article).filter(models.Article.title.ilike(f"%{req.query}%")).all()
        texts = [a.content for a in articles]
    summary = summarizer.summarize("\n".join(texts)) if texts else ""
    return {"summary": summary}


@router.post("/search", response_model=List[schemas.ArticleRead])
def search(req: schemas.SearchRequest, db: Session = Depends(get_db_session)) -> List[models.Article]:
    q = db.query(models.Article).filter(models.Article.title.ilike(f"%{req.query}%"))
    return q.all()


@router.post("/labels")
def add_label(req: schemas.LabelRequest, db: Session = Depends(get_db_session)) -> dict[str, str]:
    label = models.Label(article_id=req.article_id, name=req.name)
    db.add(label)
    db.commit()
    return {"status": "ok"}
