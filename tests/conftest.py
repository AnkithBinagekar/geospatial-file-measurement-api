import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

from app.main import create_app
from app.db.database import Base, init_db
from app.api.dependencies import get_db

# Isolated In-Memory SQLite URL
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

# StaticPool ensures the in-memory database persists across multiple sessions 
# within the same thread during testing, preventing "table not found" errors.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """Creates tables in memory before each test, yields session, and drops tables afterward."""
    # Build tables in the isolated test engine
    init_db(target_engine=engine)
    
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        # Clean up database state after each test
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db_session):
    """Provides a TestClient initialized with the mocked in-memory database."""
    # Create the app instance WITH init_database=False to guarantee no side effects
    test_app = create_app(init_database=False)
    
    def override_get_db():
        try:
            yield db_session
        finally:
            pass
            
    test_app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(test_app) as test_client:
        yield test_client
        
    test_app.dependency_overrides.clear()