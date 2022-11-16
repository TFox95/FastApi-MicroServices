from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sql_app.database import get_db
from sqlalchemy.orm import Session
from auth import schemas, models, crud



router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.get("/")
def get_auth():
    return "auth app created!"


@router.post("/create")
def createUser(request: schemas.UserCreate, db: Session = Depends(get_db)):
    
    if request.psw !=  request.re_psw:
        return JSONResponse(
            {"error": "Passwords don't match"}, status_code=status.HTTP_400_BAD_REQUEST
        )

    _user = crud.UserCRUD.create_User(db, request)

    if not _user:
        return "error"

    return _user

