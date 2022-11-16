from sqlalchemy import ForeignKey, Boolean, Column, Integer, String, UniqueConstraint as Unique, Table
from sqlalchemy.orm import relationship, backref, Session
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime

from fastapi import Depends

from sql_app.database import Base, get_db

import datetime as Date

from auth import schemas

from core.config import settings
from core.hash import Hash


class User(Base):
    __tablename__ = "users"

    pk = Column(Integer, primary_key=True, index=True, nullable=False)
    profile = relationship("Profile", back_populates="user", primaryjoin="User.pk == Profile.user_ID",
                           passive_deletes=True, uselist=False)
    uuid = Column(String(length=36), unique=True, nullable=False)

    email = Column(String(length=255), unique=True, index=True, nullable=False)
    username = Column(String(length=256), unique=True,
                      index=True, nullable=False)
    password = Column(String(length=64), nullable=False)

    isAdmin = Column(Boolean, nullable=True)
    verified = Column(Boolean, default=False, nullable=False)

    dateJoined = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    lastLogin = Column(DateTime, onupdate=func.now())

    def __repr__(self) -> str:
        return f"<User {self.username} has been created>"


class Profile(Base):
    __tablename__ = "profiles"

    pk = Column(Integer, primary_key=True, index=True, nullable=False)
    user_ID = Column(Integer, ForeignKey("users.pk", ondelete="CASCADE"))
    user = relationship("User", cascade="all,delete",
                        back_populates="profile")

    firstName = Column(String(length=20), index=True)
    lastName = Column(String(length=35), index=True)
    addresses = relationship(
        "Address", back_populates="profile", passive_deletes=True,
        primaryjoin="Profile.pk == Address.profile_pk", uselist=True)

    stripe_Cust_ID = Column(String(length=50), nullable=True)
    One_click_Purchasing = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"<Profile has been created>"


class Address(Base):
    __tablename__ = "address_book"
    pk = Column(Integer, primary_key=True, index=True, nullable=False)
    profile_pk = Column(
        Integer, ForeignKey(Profile.pk, ondelete="CASCADE"))
    profile = relationship("Profile", cascade="all,delete",
                           back_populates="addresses")
    streetNumber = Column(Integer)
    streetName = Column(String(length=100))
    aptNumber = Column(String(length=10))
    zipCode = Column(Integer)
    city = Column(String(length=25))
    state = Column(String(length=25))
    
    def __repr__(self) -> str:
        return f"<Address {self.streetNumber} {self.streetName} has been created>"
