from sqlalchemy import Column, Integer, String
from database import Base
class User(Base):
    __tablename__="users"

    uid = Column(Integer, primary_key=True)
    uname =Column(String(100))
    email =Column(String(100),unique=True)
    location=Column(String(100))


