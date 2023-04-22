from fastapi import APIRouter, Depends, status, HTTPException, Request, Cookie
from fastapi.encoders import jsonable_encoder as jEnc
from fastapi.responses import JSONResponse

from sql_app.database import get_db
from sqlalchemy.orm import Session

from auth import schemas, models, crud
from core.config import JsonRender

NAMESPACE = f"Auth Routes"

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

UserModel = models.User

@router.get("/")
def get_auth():
    return "auth app created!"


@router.post("/register")
def Register(request: schemas.UserCreate, db: Session = Depends(get_db)):

    dbEmailQuery: UserModel = db.query(UserModel).filter(
        UserModel.email == request.email).scalar() or None
    dbUsernameQuery: UserModel = db.query(UserModel).filter(
        UserModel.username == request.username).scalar() or None

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
def login(request: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    This function only recieves data as Form data returns a jwt token
    """
    user: UserModel = crud.UserCRUD.retrieve_User(db, email=request.username) if "@" in str(request.username
                                                                                        ) else crud.UserCRUD.retrieve_User(db, username=request.username)
    checkPassword = crud.AuthHandler().verify_password(psw=request.password, hashed_psw=user.password) if (user
                                                                                                            ) else None

    if not checkPassword:
        return JSONResponse(
            {"error": "Password or Username doesn't match; Check credintials and retry"},
            status.HTTP_409_CONFLICT
        )

    jwt = crud.AuthHandler().encode_token(user.UUID, user.username)
    content = {"success": {"username": f"{user.username}", "token" : f"bearer {jwt}"}}
    res = JSONResponse(content, status_code=status.HTTP_302_FOUND)
    res.set_cookie(key="Authorization", value=jwt, secure=True, httponly=True)
    return res


async def checkAuthorization(request: Request,Authorization=Cookie(None)) -> str:

    try:
        Authorization = Authorization if Authorization else str(
        request.headers["Authorization"]).split(" ")[-1] if not None else None
        if not Authorization:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="No token found")
        return Authorization
        
    except:
        raise HTTPException(detail={"error": f"Token invalid"}, status_code=status.HTTP_401_UNAUTHORIZED)

    

async def getCurrentUser(token = Depends(checkAuthorization), db:Session = Depends(get_db)) -> UserModel:
    try:
        decodedToken: dict= crud.AuthHandler().decode_token(token)
        decodedUser = crud.UserCRUD.retrieve_User(db, username=decodedToken.get("username"))
        return decodedUser
    except:
        raise HTTPException(detail={"error": "Internal Error"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get("/protected")
async def protectedRoute(decoded=Depends(getCurrentUser)):
    data = decoded

    if data:
        return JSONResponse({"success": "lets go!"}, status_code=status.HTTP_200_OK)

    return JSONResponse({"error": "uhh some went wrong!"}, status_code=status.HTTP_400_BAD_REQUEST)


@router.post("/logout")
async def logout( decoded:dict=Depends(getCurrentUser)):
    username =  decoded.get("username")
    content = {"success" : f"{username} has been Logged out"}
    res = JSONResponse(content, status.HTTP_202_ACCEPTED)
    res.delete_cookie("Authorization")
    return res


@router.get("/retrieve_user", response_model=schemas.UserBase, response_model_exclude=["pk", "UUID", "isAdmin"], response_class=JsonRender)
async def retrieveUserData(request: Request, User= Depends(getCurrentUser)) -> schemas.UserBase:
    return User

@router.get("/retrieve_user/all")
async def retrieveAllUserData(request: Request, User= Depends(getCurrentUser)) -> schemas.UserBase:
    decodedUser = jEnc(User)
    content = {"success": decodedUser}
    return JSONResponse(content, status.HTTP_200_OK)