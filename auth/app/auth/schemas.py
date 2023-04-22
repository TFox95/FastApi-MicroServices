from pydantic import BaseModel as Base, EmailStr
from datetime import datetime
from typing import Union


class AddressBase(Base):
    streetNumber: Union[int , None] 
    streetName: Union[str , None] = None
    aptNumber: Union[str , None] = None

    ZipCode: Union[int , None]
    city: Union[str , None] = None
    state: Union[str , None] = None


class AddressCreate:
    profile_pk: int


class ProfileBase(Base):
    firstName: Union[str , None] = None
    lastName: Union[str , None] = None
    addresses: list[AddressBase] = []

    stripe_Cust_ID: Union[str , None] = None
    One_click_Purchasing: Union[bool , None] = None


class ProfileCreate(ProfileBase):
    user_UUID: int


class UserLogin(Base):
    username: str
    password: str


class UserBase(Base):
    email: EmailStr
    username: str
    UUID: Union[str , None] = None
    pk: Union[int , None]
    
    verified: bool = False
    isAdmin: bool = False

    dateJoined: Union[datetime , str , None]
    lastLogin: Union[datetime , str , None] = None

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    psw: str
    re_psw: str


class User(UserBase):
    pk: int
    lastLogin: datetime

class Token(Base):
    exp: int
    iat: int
    iss: str
    uuid: str
    username: str