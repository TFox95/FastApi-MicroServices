from fastapi import APIRouter, HTTPException, Depends, status, Request, Body, Header
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder as jEnc
from sqlalchemy.orm import Session
from sql_app.database import get_db

router = APIRouter(
    prefix="/db", 
    tags=["database"]
)


@router.get("/")
async def get_sql_app(res=JSONResponse, req=Request, db: Session = Depends(get_db)):

    try:
        content = "Database was successful reached"
        return res({"sucess": content}, status.HTTP_201_CREATED)

    except Exception as e:
        raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, f"{jEnc(e)}")
