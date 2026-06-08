from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from config.database import Base

# SQLAlchemy Employee Model (Database Table)
class Employee(Base):
    __tablename__ = "employees"
    
    eid = Column(Integer, primary_key=True, index=True)
    ename = Column(String(100), nullable=False)
    esal = Column(Float, nullable=False)
    loc = Column(String(100), nullable=False)

# Pydantic Model for API Request/Response
class EmployeeSchema(BaseModel):
    eid: int
    ename: str
    esal: float
    loc: str
    
    class Config:
        from_attributes = True 


    