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


'''
usage: fetch user by Id
Rest API URL: http://localhost:8000/read/101
Method Type: GET
Required Fields:None
Access Type:Public
'''

@app.get("/read/{uid}",response_model=UserResponse)
def get_user_id(uid:int,db:Session = Depends(get_db)):
    user=db.query(User).filter(User.uid == uid).first()

    if not user:
        raise HTTPException(status_code=404,detail="User Not Found")
    return user 


'''
usage: update user by id
Rest API URL: http://localhost:8000/update/101
Method Type: PUT
Required Fields:uname,email,location
Access Type:Public
'''

@app.put("/update/{uid}",response_model=UserResponse)
def update_user(uid:int,update_user:UserCreate,db:Session=Depends(get_db)):
    print(update_user)
    user=db.query(User).filter(User.uid == uid).first()

    if not user:
        raise HTTPException(status_code=404,detail="User Not Found")
    
    user.uname=update_user.uname
    user.email=update_user.email 
    user.location=update_user.location

    db.commit()
    db.refresh(user)

    return user



'''
usage: delete user by id
Rest API URL: http://localhost:8000/delete/101
Method Type: DELETE
Required Fields:None
Access Type:Public
'''

@app.delete("/delete/{uid}")
def delete_user(uid:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.uid == uid).first()

    if not user:
        raise HTTPException(status_code=404,detail="User Not Found")


    print(user.__dict__)
    db.delete(user)
    db.commit()

    return {"msg":"Deleted Successfully"}







