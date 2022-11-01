from fastapi import APIRouter, HTTPException, Depends, status, Request, Body, Header
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sql_app.database import get_db
from core import logging

router = APIRouter()


@router.get("/db/conn")
async def get_sql_app(res= JSONResponse,req = Request, db: Session= Depends(get_db)):

    try:
        if  db:
            print(db.connection())
            hellow: str = "helloworld"
            return res({"sucess": hellow}, status.HTTP_201_CREATED)
        
        return res({"error": {
            HTTPException(status.HTTP_400_BAD_REQUEST, {"token":f"Bearer {hellow}", "crazy": "Nutssafbousgjnel"})
        }})
    
    except Exception as e:
        print(e)
        return res({"error": "Opps, something went wrong."}, status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/create")
async def letmeesee(payload: dict= Body(), res= JSONResponse, db: Session= Depends(get_db)):
    return {"success":payload}