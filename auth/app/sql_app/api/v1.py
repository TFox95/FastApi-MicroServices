from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_sql_app():
    return "sql_app app created!"
