from fastapi import APIRouter, Depends,HTTPException 

from sqlalchemy.orm import Session

from database.db import get_db
from models.user_model import User 

router=APIRouter(prefix="/users", tags=["users"]) 


#Fetch All Users

#Fetch User By Id 

#Delet User by Id