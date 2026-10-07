from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Geospatial File Measurement API"
    DATABASE_URL: str = "sqlite:///./geospatial.db"
    
    # Future Stage 2/3 settings can be added here (e.g., MAX_UPLOAD_SIZE)

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()