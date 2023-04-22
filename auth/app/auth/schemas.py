from pydantic import BaseModel as Base, EmailStr
from datetime import datetime


class AddressBase(Base):
    streetNumber: int 
    streetName: str
    aptNumber: str

    ZipCode: int
    city: str
    state: str


class AddressCreate:
    profile_pk: int


class ProfileBase(Base):
    firstName: str | None
    lastName: str | None
    addresses: list[AddressBase] = []

    stripe_Cust_ID: str | None
    One_click_Purchasing: bool | None


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