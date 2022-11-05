from fastapi import APIRouter, HTTPException, Depends, status, Request, Body, Header
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sql_app.database import get_db
from core import logging

router = APIRouter(
    prefix="/db", 
    tags=["database"]
)


@router.get("/")
async def get_sql_app(res=JSONResponse, req=Request, db: Session = Depends(get_db)):

    try:
        if not db:
            raise Exception(db)
            
        print(db.connection())
        hellow: str = "helloworld"
        return res({"sucess": hellow}, status.HTTP_201_CREATED)

    except Exception as e:
        print(e)
        return res({"error": {"Opps, something went wrong.",
                              status.HTTP_500_INTERNAL_SERVER_ERROR}},
                   status.HTTP_500_INTERNAL_SERVER_ERROR)
