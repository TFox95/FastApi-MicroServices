from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from core import logging

router = APIRouter()


@router.get("/")
async def get_sql_app(db: Session= Depends(main.get_db), res= JSONResponse):

    try:
        if  db:
            print(db.connection())
            hellow: str = "helloworld"
            return res({"sucess": hellow}, 201)
        
        return res({"error": {
            HTTPException(status.HTTP_400_BAD_REQUEST, {"token":f"Bearer {hellow}", "crazy": "Nutssafbousgjnel"})
        }})
    
    except Exception as e:
        print(e)
        return res({"error": "Opps, something went wrong."}, status.HTTP_500_INTERNAL_SERVER_ERROR)

