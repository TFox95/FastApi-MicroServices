import jwt 
from fastapi import HTTPException, status
from uuid import uuid4

from datetime import timedelta, datetime

from pydantic import EmailStr
from sqlalchemy.orm import Session
from sql_app.database import get_db

from auth import schemas, models

from core import logging
from core.hash import Hash
from core.config import settings
from core.logging import ServerINFO

NAMESPACE:str = "Auth CRUD"
UserModel = models.User
TokenSchema = schemas.Token

class AuthHandler():
    Secret = settings.AUTH_SECRET
    Pepper = settings.PEPPER
    

    def get_password_hash(self, psw: str) -> str:
        return Hash.encode(key=psw, pepper=self.Pepper)
    
    def verify_password(self, psw, hashed_psw) -> bool:
        pswKeyHash = self.get_password_hash(psw)
        return Hash.verify(key=pswKeyHash,encoded_key=hashed_psw,pepper=self.Pepper)
        
    def encode_token(self, uuid:str, username:str):
        payload = {
            "iss": "https://www.Aestriks.com",
            "exp": datetime.utcnow() + timedelta(days=100, hours=0, minutes=0),
            "iat": datetime.utcnow(),
            "uuid": uuid,
            "username": username 
        }
        return jwt.encode(
            payload,
            self.Secret,
            algorithm="HS256"
        )
    
    def decode_token(self, token) -> TokenSchema:
        try:
            payload = jwt.decode(
                token,
                self.Secret,
                algorithms="HS256"
            )
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Signature has expired')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
            
        return payload
    
    def grant_access(self, token:str, uuid:str):            
            decoded = self.decode_token(token)
            if not uuid == decoded.uuid:
                return False
                
            return True

class UserCRUD():
    
    def create_User(db:Session, request: schemas.UserCreate) -> UserModel:
        """
        function to create a user instance & a linked user 
        profile instance
        
        """
        _dict: dict = request.dict()
        _dict["uuid"] = f"user_{uuid4()}"
        _dict["psw"] = AuthHandler().get_password_hash(psw=_dict.get("re_psw")) 
        _dict.pop("re_psw", None)
        
        _user: UserModel = UserModel(email=_dict.get("email"), username=_dict.get("username"),
                    password=Hash.encode(_dict.get("psw"), settings.PEPPER), UUID=_dict.get("uuid"),
                    verified=_dict.get("verified"), isAdmin=_dict.get("isAdmin"))
        _profile = models.Profile(user_UUID=_user.UUID)
        #adding User & User's Profile to db and then refreshing the _user instance with the updated information
        db.add_all([_user, _profile])
        db.commit()
        db.refresh(_user)
        ServerINFO(NAMESPACE, f"<User {_user.username} has been created! Successfully!>")
        return _user
    
    def retrieve_User(db:Session, username:str = None, email:EmailStr = None) -> UserModel:
        
        _retrieve_user = db.query(UserModel).filter(UserModel.username == username).scalar() if (username
                    ) else db.query(UserModel).filter(UserModel.email == email).scalar() if (email
                        ) else None
        return _retrieve_user
    
    def lastLogin (db:Session, username:str) -> bool:
        updateUserData = db.query(UserModel).filter(
            UserModel.username == username).update({
            "lastLogin": datetime.now()
            })
        if not updateUserData:
            return False
        db.commit()
        return True


