from fastapi import APIRouter, Depends, status, HTTPException, Request, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sql_app.database import get_db
from sqlalchemy.orm import Session

from auth import schemas, models, crud

NAMESPACE = f"Auth Routes"

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

User = models.User

Oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


@router.get("/")
def get_auth():
    return "auth app created!"


@router.post("/create", response_model_exclude={"password", "pk", "isAdmin"})
def Register(request: schemas.UserCreate, db: Session = Depends(get_db)):
    
    dbEmailQuery:User = db.query(User).filter(User.email == request.email).scalar() or None
    dbUsernameQuery: User = db.query(User).filter(User.username == request.username).scalar() or None
    
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

    return JSONResponse({
        "success": f"User, {_user.username}, has been created!"
    }, status.HTTP_201_CREATED)

@router.post("/token")
def login(formData: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    This function only recieves data as Form data returns a jwt token
    """
    
    user: User = crud.UserCRUD.retrieve_User(db, email=formData.username) if "@" in str(formData.username
        ) else crud.UserCRUD.retrieve_User(db, username=formData.username)
    checkPassword = crud.AuthHandler().verify_password(psw=formData.password, hashed_psw=user.password)
    
    return checkPassword