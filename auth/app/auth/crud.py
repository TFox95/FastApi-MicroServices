from uuid import uuid4

from sqlalchemy.orm import Session
from sql_app.database import get_db, engine

from auth import (schemas, models)

from core import logging
from core.hash import Hash
from core.config import settings
from core.logging import ServerINFO

NAMESPACE = str("Auth CRUD")
User = models.User

class UserCRUD():
    
    def create_User(db:Session, request: schemas.UserCreate):
        
        _dict: dict = request.dict()
        _dict["uuid"] = uuid4()
        _dict["psw"] = Hash.encode(_dict.get("re_psw"), settings.PEPPER) 
        _dict.pop("re_psw", None)
        _user = User(email=_dict.get("email"), username=_dict.get("username"),
                    password=Hash.encode(_dict.get("psw"), settings.PEPPER), uuid=_dict.get("uuid"),
                    verified=_dict.get("verified"), isAdmin=_dict.get("isAdmin"))
        #adding User to db and then refreshing the _user instance with the updated information
        db.add(_user)
        db.commit()
        db.refresh(_user)
        #Using the refreshed _user instance pk
        _profile = models.Profile(user_ID=_user.pk)
        db.add(_profile)
        db.commit()
        logging.ServerINFO(NAMESPACE, f"<User {_user.username} has been created! Successfully!>")
        return _user

    def retrieve_User(db:Session):
        pass

