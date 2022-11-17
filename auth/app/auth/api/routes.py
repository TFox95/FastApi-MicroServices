from fastapi import APIRouter, Depends, status, HTTPException
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


@router.post("/create", response_model_exclude={"password", "pk", "isAdmin"})
def Register(request: schemas.UserCreate, db: Session = Depends(get_db)):
    
    dbEmailQuery:User = db.query(User).filter(User.email == request.email).first() or None
    dbUsernameQuery: User = db.query(User).filter(User.username == request.username).first() or None

    if dbEmailQuery or dbUsernameQuery or (request.psw != request.re_psw):
        if dbEmailQuery:
            return JSONResponse(
                {"error": f"Email, {dbEmailQuery.email}, is already in use"}, status_code=status.HTTP_409_CONFLICT
            )
        
        if dbUsernameQuery:
            return JSONResponse(
                {"error": f"Username, {dbUsernameQuery.username}, is already in use"}, status_code=status.HTTP_409_CONFLICT
            )
        
        return JSONResponse(
            {"error": "Passwords don't match; Passwords must be the same"}, status_code=status.HTTP_409_CONFLICT
        )

    _user = crud.UserCRUD.create_User(db, request)

    if not _user:
        return "error"

    return JSONResponse({
        "success": {_user}
    }, status.HTTP_201_CREATED)

