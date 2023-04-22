from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from core import logging
from core.config import settings

from sql_app.database import engine
from auth import models as aModels

from sql_app.api import routes as sql_routes
from auth.api import routes as auth_routes

import time

aModels.User.metadata.create_all(engine)
aModels.Profile.metadata.create_all(engine)
aModels.Address.metadata.create_all(engine)

NAMESPACE: str = f"Base Server"


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME,
                    description="MicroService for handling Authentication",
                    version="0.3.1"
                    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin)
                       for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["POST", "PATCH", "GET", "DELETE", "PUT", "OPTIONS"],
        allow_headers=["Access-Control-Allow-Headers", "Origin", "X-Requested-Width", "Content-Type", "Accept", "Authorization"],
        
    )
    return _app

app = get_application()


# Error Handling
@app.middleware("http")
async def errors_handling(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        return JSONResponse(status_code=500, content={'reason': str(exc)})


# Creates Header named X-Process-Time to report the time to a calls completion.
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(f"{process_time}/s")
    return response


#Routes
app.include_router(sql_routes.router)
app.include_router(auth_routes.router)