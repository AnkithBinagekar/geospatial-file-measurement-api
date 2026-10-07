from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings

# check_same_thread=False is required so FastAPI can reuse SQLite connections across threads
engine = create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def init_db(target_engine=engine):
    """
    Creates all tables in the database.
    Accepts an optional target_engine for dependency injection during test setup.
    """
    # STRICT REQUIREMENT: Import models before calling create_all 
    # to guarantee Base.metadata is populated with our schemas.
    from app.db import models 
    
    Base.metadata.create_all(bind=target_engine)