from fastapi import FastAPI, Depends, HTTPException
from database import SessionLocal, engine
import models 
from models import User
from schemas import UserCreate,UserResponse 
from sqlalchemy.orm import Session

#if table not exits- 
models.Base.metadata.create_all(bind=engine)


app=FastAPI()


#Database Dependency 
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


'''
usage: Application Root
Rest API URL: http://localhost:8000/
Method Type: GET
Required Fields:None
Access Type:Public
'''

@app.get("/")
def index_page():
    return {"msg":"Appliation Root Request"}



'''
usage: create new user
Rest API URL: http://localhost:8000/create
Method Type: POST
Required Fields:uname,email,location
Access Type:Public
'''

@app.post("/create/",response_model=UserResponse)
def create_user(user:UserCreate,db:Session=Depends(get_db)):
    db_user=User(uname=user.uname,email=user.email,location=user.location)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



'''
usage: fetch all users
Rest API URL: http://localhost:8000/read
Method Type: GET
Required Fields:None
Access Type:Public
'''
@app.get("/read/")
def get_users(db:Session=Depends(get_db)):
    return db.query(User).all()


def get_user_id():
    pass 

def update_user():
    pass 

def delete_user():
    pass 



'''
usage: fetch user by Id
Rest API URL: http://localhost:8000/read/101
Method Type: GET
Required Fields:None
Access Type:Public
'''



'''
usage: update user by id
Rest API URL: http://localhost:8000/update/101
Method Type: PUT
Required Fields:uname,email,location
Access Type:Public
'''


'''
usage: delete user by id
Rest API URL: http://localhost:8000/delete/101
Method Type: DELETE
Required Fields:None
Access Type:Public
'''