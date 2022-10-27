from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_config():
    return "config app created!"
