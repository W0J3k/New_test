CREATE EXTENSION IF NOT EXISTS vector;

-- Example indexes
CREATE TABLE IF NOT EXISTS articles (
  id SERIAL PRIMARY KEY,
  title TEXT,
  content TEXT,
  embedding vector(384),
  tsv tsvector
);

CREATE INDEX IF NOT EXISTS idx_articles_tsv ON articles USING GIN(tsv);
CREATE INDEX IF NOT EXISTS idx_articles_embedding ON articles USING ivfflat (embedding vector_cosine_ops) WITH (lists=100);
