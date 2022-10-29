from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core import logging
from core.config import settings

NAMESPACE: str = f"Base Server"


def get_application():
    _app = _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin)
                       for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    logging.ServerINFO(NAMESPACE, f"Server Running, MicroServer: {_app.title}")
    return _app


app = get_application()
