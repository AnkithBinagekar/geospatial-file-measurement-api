from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings
from app.db.database import init_db

def create_app(init_database: bool = True) -> FastAPI:
    """
    Application factory.
    Allows tests to create an isolated app instance without side effects.
    """
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # Startup phase
        if init_database:
            # Initialize production/local SQLite database tables when the server starts
            init_db()
        yield
        # Shutdown phase (cleanups can go here if needed in the future)

    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="API for processing and measuring Geospatial files.",
        version="1.0.0",
        lifespan=lifespan
    )

    app.include_router(router)
    return app

# Default global app instance for Uvicorn
# Because we use lifespan, simply importing `app` will NOT create the database.
app = create_app(init_database=True)