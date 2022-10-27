import dotenv
from os import getenv
from typing import List

from pydantic import AnyHttpUrl

dotenv.load_dotenv()

class Settings():
    PROJECT_NAME: str = getenv("PROJECT_NAME") or "test"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        getenv("BACKEND_CORS_ORIGINS")] or None
    BACKEND_PORT: int = int(getenv("UVICORN_PORT")) or 8000


settings = Settings()
