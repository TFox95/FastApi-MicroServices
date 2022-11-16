from uuid import uuid4

import sqlalchemy
from sqlalchemy.orm import Session, Query
from sqlalchemy import select

from sql_app.database import get_db, engine

from auth import (schemas, models)

from core import logging
from core.hash import Hash
from core.config import settings
from core.logging import ServerINFO

User = models.User
connection = engine.connect()

NAMESPACE = str("/Auth/CRUD")

class UserCRUD():
    
    def create_User(db:Session, request: schemas.UserCreate):
        #e = Session.query(User)
        
        query = select(User).where(User.username == request.username)
        conn = connection.execute(query).first()
        #print(query)
        print(conn)
        
        
        _dict: dict = request.dict()
        _dict["uuid"] = uuid4()
        _dict["psw"] = Hash.encode(_dict.get("re_psw"), settings.PEPPER) 
        _dict.pop("re_psw", None)
        _user = User(email=_dict.get("email"), username=_dict.get("username"),
                    password=Hash.encode(_dict.get("psw"), settings.PEPPER), uuid=_dict.get("uuid"),
                    verified=_dict.get("verified"), isAdmin=_dict.get("isAdmin"))
    
        db.add(_user)
        db.commit()
        db.refresh(_user)
        logging.ServerINFO(NAMESPACE, f"<User {_user.username} has been created! Successfully!")
        return _user
    