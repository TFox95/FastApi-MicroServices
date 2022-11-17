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

    DB_USER: str = getenv("DB_USER")
    DB_PASS: str = getenv("DB_PASS")
    DB_NAME: str = getenv("DB_NAME")
    DB_HOST: str = getenv("DB_HOST")
    DB_PORT: int = getenv("DB_PORT")
    DB_DRIVER: str = getenv("DB_DRIVER")
    DB_URL: str = f"{DB_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    PEPPER: str = getenv("HASH_PEPPER")
    SALT: str | float = getenv("HASH_SALT")

settings = Settings()
