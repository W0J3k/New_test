from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.core.logging import init_logging
from app.api import routes
from app.db import models
from app.db.session import engine

settings = get_settings()
init_logging()

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="MyInfo_pro API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.backend_cors_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(routes.router)
