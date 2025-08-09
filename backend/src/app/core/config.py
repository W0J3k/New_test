from pydantic import BaseSettings, Field
from functools import lru_cache


class Settings(BaseSettings):
    database_url: str = Field(
        default="sqlite+pysqlite:///./test.db", env="DATABASE_URL"
    )
    redis_url: str = Field(default="redis://localhost:6379/0", env="REDIS_URL")
    backend_cors_origins: str = Field(
        default="*", env="BACKEND_CORS_ORIGINS"
    )
    openai_api_key: str | None = Field(default=None, env="OPENAI_API_KEY")
    ollama_base_url: str = Field(
        default="http://localhost:11434", env="OLLAMA_BASE_URL"
    )
    secret_key: str = Field(default="secret", env="SECRET_KEY")

    class Config:
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    return Settings()
