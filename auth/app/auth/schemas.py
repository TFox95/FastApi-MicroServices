from pydantic import BaseModel as Base, EmailStr
from sqlalchemy.orm import Session
from uuid import uuid4
from auth import models
from datetime import datetime


class AddressBase(Base):
    streetNumber: int | None = None 
    streetName: str | None = None
    aptNumber: str | None = None

    ZipCode: int | None = None
    city: str | None = None
    state: str | None = None


class AddressCreate:
    profile_pk: int


class ProfileBase(Base):
    firstName: str | None = None
    lastName: str | None = None
    addresses: list[AddressBase] = []

    stripe_Cust_ID: str | None = None
    One_click_Purchasing: bool | None = None


class ProfileCreate(ProfileBase):
    user_ID: int


class UserBase(Base):
    email: EmailStr
    username: str
    uuid: str | None = None
    
    verified: bool = False
    isAdmin: bool = False


class UserCreate(UserBase):
    psw: str
    re_psw: str


class User(UserBase):
    pk: int
    lastLogin: datetime

