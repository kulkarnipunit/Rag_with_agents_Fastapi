
import os

class Settings:
    PROJECT_NAME = "Personal Context AI"
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/context_ai")

settings = Settings()
