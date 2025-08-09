from sqlalchemy.orm import Session
from fastapi import Depends

from app.db.session import get_db


def get_db_session(db: Session = Depends(get_db)) -> Session:
    return db
