from uvicorn import run, main
from core.config import settings

if __name__ == "__main__":

    run("main:app", port=settings.BACKEND_PORT, 
        reload=True, debug=True)