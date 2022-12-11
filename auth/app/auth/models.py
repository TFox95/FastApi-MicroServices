from sqlalchemy import (ForeignKey, Boolean, 
                        Column, Integer,
                        String)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime

from sql_app.database import Base


class User(Base):
    __tablename__ = "users"

    pk = Column(Integer, primary_key=True, index=True, nullable=False)
    profile = relationship("Profile", back_populates="user", primaryjoin="User.UUID == Profile.user_UUID",
                           passive_deletes=True, uselist=False)
    UUID = Column(String(length=41), unique=True, nullable=False)

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
        return f"{self.username}"


class Profile(Base):
    __tablename__ = "user_profiles"

    pk = Column(Integer, primary_key=True, index=True, nullable=False)
    user_UUID = Column(String(length=41),ForeignKey("users.UUID", ondelete="CASCADE"))
    user = relationship("User", cascade="all,delete",
                        back_populates="profile")

    firstName = Column(String(length=20), index=True)
    lastName = Column(String(length=35), index=True)
    addresses = relationship(
        "Address", back_populates="profile", passive_deletes=True,
        primaryjoin="Profile.pk == Address.profile_pk", uselist=True)

    stripe_Cust_ID = Column(String(length=50), nullable=True)
    One_click_Purchasing = Column(Boolean, default=False)



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
