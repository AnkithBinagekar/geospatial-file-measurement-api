from typing import Generator
from sqlalchemy.orm import Session
from app.db.database import SessionLocal

def get_db() -> Generator[Session, None, None]:
    """
    FastAPI Dependency that yields a database session for a single request,
    ensuring safe closure after the request finishes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()