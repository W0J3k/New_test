from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), index=True)
    name = Column(String(255))
    url = Column(String(500), unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    articles = relationship("Article", back_populates="source")


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(Integer, ForeignKey("sources.id"))
    url = Column(String(500), unique=True, index=True)
    title = Column(String(500))
    content = Column(Text)
    retrieved_at = Column(DateTime, default=datetime.utcnow)
    summary_text = Column(Text)

    source = relationship("Source", back_populates="articles")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey("articles.id"))
    platform = Column(String(50))
    external_id = Column(String(255), index=True)


class Entity(Base):
    __tablename__ = "entities"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    type = Column(String(50))


class Enrichment(Base):
    __tablename__ = "enrichments"

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey("articles.id"))
    key = Column(String(255))
    value = Column(Text)


class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey("articles.id"))
    text = Column(Text)


class Label(Base):
    __tablename__ = "labels"

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey("articles.id"))
    name = Column(String(255))
