from sqlalchemy import ForeignKey, Boolean, Column, Integer, String, null, UniqueConstraint
from sqlalchemy.orm import relationship

from SQL_APP.Database import Base

class User(Base):
    __tablename___ = "users"

    id = 
    uuid = 

    firstName =
    lastName =

    email = 
    username = 
    password = 

    isActive =
    lastLogin = 
    dateJoined = 
    