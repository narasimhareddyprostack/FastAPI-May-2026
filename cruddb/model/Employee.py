from pydantic import BaseModel
#Employee Model  ---- MongoDB Collection / Mysql Table
class Employee(BaseModel):
    eid:int 
    ename:str
    esal:float
    loc:str 


    