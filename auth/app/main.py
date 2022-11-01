from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core import logging
from core.config import settings
from sql_app.api import v1

NAMESPACE: str = f"Base Server"


def get_application():
    _app = _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin)
                       for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["POST", "PATCH", "GET", "DELETE", "PUT", "OPTIONS"],
        allow_headers=["Access-Control-Allow-Headers", "Origin", "X-Requested-Width", "Content-Type", "Accept", "Authorization"],
        
    )
    logging.ServerINFO(NAMESPACE, f"Server Running, MicroServer: {_app.title}")
    return _app


app = get_application()

app.include_router(v1.router)