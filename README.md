# MyInfo_pro

MyInfo_pro is an information-gathering web application that aggregates news, public data, Reddit posts and Telegram messages. Content is normalized, deduplicated and stored with embeddings to enable hybrid search and summarisation.

## Architecture

```
Browser -> Next.js frontend -> FastAPI backend -> PostgreSQL/pgvector
                                    |                 \
                                    |-- Redis (RQ) ---- workers
```

## Quickstart

```bash
cp .env.example .env
docker compose up --build
# in another terminal after containers are running
poetry run pytest            # backend tests
```

Seed the database with sources:

```bash
curl -X POST http://localhost:8000/sources -H 'Content-Type: application/json' \
  -d '{"type":"rss","name":"ABC News","url":"https://www.abc.net.au/news/feed/51120/rss.xml"}'
```

### Adding a new source
1. POST to `/sources` with type (`rss`, `website`, `reddit`, `telegram`).
2. Workers will poll based on `app/config/scheduler.py` definitions.

### Enabling Ollama summariser
1. Install [Ollama](https://ollama.ai) and run `ollama run mistral`.
2. Ensure `OLLAMA_BASE_URL` in `.env` points to the Ollama host.

## Compliance
* Respect robots.txt and site terms of use.
* Identify with a descriptive User-Agent string when crawling.
* Apply per-source rate limits.

## Roadmap
* ML-based misinformation detection via pluggable model API.
* Email/Telegram digests and advanced analytics.
