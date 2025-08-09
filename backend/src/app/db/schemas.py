from datetime import datetime
from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class SourceCreate(BaseModel):
    type: str
    name: str
    url: HttpUrl


class SourceRead(SourceCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ArticleRead(BaseModel):
    id: int
    source_id: int
    url: HttpUrl
    title: str
    content: str
    retrieved_at: datetime

    class Config:
        from_attributes = True


class SummarizeRequest(BaseModel):
    ids: Optional[List[int]] = None
    query: Optional[str] = None


class SearchRequest(BaseModel):
    query: str


class LabelRequest(BaseModel):
    article_id: int
    name: str
