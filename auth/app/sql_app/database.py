from core.config import settings

import sqlalchemy

def connnectMysqlDatabase() -> sqlalchemy.engine.base.Engine:
    
    pool = sqlalchemy.engine.url.URL.create(
        drivername=settings.DB_DRIVER,
        username=settings.DB_USER,
        password=settings.DB_PASS,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME
    )

    print(f"database connection is {pool}")

    return pool