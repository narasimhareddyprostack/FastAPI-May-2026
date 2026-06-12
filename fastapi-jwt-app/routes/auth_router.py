from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session 
from schemas.user_schema import UserCreate,UserLogin
from database.db import get_db
from models.user_model import User
#from utils.auth import hash_password
router=APIRouter(prefix="/auth")

'''
Usage: User Registration
Rest API URL: http://localhost:8000/auth/register 
Method:POST
Required  Field:name,email,password
Access Type:public
'''
@router.post("/register")
def user_register(user:UserCreate,db:Session=Depends(get_db)):
    db_user=db.query(User).filter(User.email==user.email).first()

    if db_user:
        raise HTTPException(status_code=404,detail="Email/User Already Exits")
    

    
    
    new_user=User(name=user.name,
                 email=user.email,
                 password=user.password
    )
    
    db.add(new_user)
    db.commit()
    return {"msg":"New User Created Successfully"}

