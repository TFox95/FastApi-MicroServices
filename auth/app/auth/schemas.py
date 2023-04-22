from pydantic import BaseModel as Base, EmailStr
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
    user_UUID: int


class UserLogin(Base):
    username: str
    password: str


class UserBase(Base):
    email: EmailStr
    username: str
    UUID: str | None = None
    pk: int | None
    
    verified: bool = False
    isAdmin: bool = False

    dateJoined: datetime | str | None
    lastLogin: datetime | str | None = None

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