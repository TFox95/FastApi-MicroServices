import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker

from core.config import settings

NAMESPACE: str = "SQL_APP/Database"

engine = create_engine(url="postgresql://admin_ikuyo:a6TBOtNYqhPXXD2O5PzOxXvFI8YP2wNT@dpg-ch1jiq5gk4qarql97dh0-a/e_commerce_1cyi", echo=False)

SessionCloud = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()

def get_db():
    db = SessionCloud()
    try:
        yield db
    finally:
        db.close()
