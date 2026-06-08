from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class User(Base):
    __tablename__="users"

    uid = Column(Integer, primary_key=True)
    uname =Column(String(100))
    email =Column(String(100),unique=True)
    location=Column(String(100))

'''
Here User inherits from Base, 
allowing SQLAlchemy to create and manage the users table.
'''