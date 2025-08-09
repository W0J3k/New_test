from redis import Redis
from rq import Queue
from app.core.config import get_settings

settings = get_settings()
redis = Redis.from_url(settings.redis_url)
queue = Queue("default", connection=redis)
