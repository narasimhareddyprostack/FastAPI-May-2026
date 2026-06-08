from pydantic import BaseModel 

class UserCreate(BaseModel):
    uname:str
    email:str 
    location:str


class UserResponse(UserCreate):
    uid:int 
    
    class Config:
        from_attribute=True