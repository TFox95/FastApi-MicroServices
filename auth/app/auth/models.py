from sqlalchemy import ForeignKey, Boolean, Column, Integer, String, UniqueConstraint as Unique, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime

from sql_app.database import Base
import datetime as Date


class User(Base):
    __tablename__ = "users"

    pk = Column(Integer, primary_key=True, index=True, nullable=False)
    uuid = Column(String(length=36), unique=True, nullable=False)
    profile = relationship("Profile", backref="user", passive_deletes=True)

    email = Column(String(length=255), unique=True, index=True, nullable=False)
    username = Column(String(length=25), unique=True, index=True, nullable=False)
    password = Column(String(length=35), nullable=False)

    isStaff = Column(Boolean, nullable=True)
    isAdmin = Column(Boolean, nullable=True)
    verified = Column(Boolean, default=False, nullable=False)
    isActive = Column(Boolean, default=False)

    dateJoined = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    lastLogin = Column(DateTime, onupdate=func.now())

    def __init__(self, username) -> None:
        profile = Profile(self, username)
        
        

class Profile(Base):
    __tablename__ = "profiles"

    pk = Column(Integer, primary_key=True, index=True, nullable=False)
    userId = relationship(Integer, ForeignKey(User.pk, ondelete="CASCADE"))
    user = relationship("User", cascade= "all,delete", backref="profile")

    firstName = Column(String(length=20), index=True)
    lastName = Column(String(length=35), index=True)

    streetAddress = Column(String(length=100))
    ZipCode = Column(Integer)
    city = Column(String(length=25))
    state =Column(String(length=25)) 
