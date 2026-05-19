from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from model.Employee import Employee as EmployeeModel

# Create API Router for Employee Operations
emprouter = APIRouter(prefix="/emp", tags=["Employee"])

# MongoDB collection
client = MongoClient('mongodb://localhost:27017/')
db = client['dbone']
emp_col = db['employees']


'''
usage: Create Employee
Rest API URL: http://127.0.0.1:8000/emp/create
Method Type: POST
Required Fields: eid, ename, esal, loc
Access Type: Public
'''
@emprouter.post("/create")
def create_employee(emp: EmployeeModel):
    emp_col.insert_one(emp.dict())
    return {"msg": "New Employee Created Successfully"}


'''
usage: Get all Employees
Rest API URL: http://127.0.0.1:8000/emp/read
Method Type: GET
Required Fields: None
Access Type: Public
'''
@emprouter.get("/read")
def get_employees():
    employees = list(emp_col.find({}, {"_id": 0}))
    return employees


'''
usage: Get Employee by id
Rest API URL: http://127.0.0.1:8000/emp/101
Method Type: GET
Required Fields: None
Access Type: Public
'''
@emprouter.get("/{eid}")
def get_emp_by_id(eid: int):
    employee = emp_col.find_one({"eid": eid}, {"_id": 0})
    
    if not employee:
        raise HTTPException(status_code=404, detail="Employee Not Found")
    return employee


'''
usage: Update Employee
Rest API URL: http://127.0.0.1:8000/emp/101
Method Type: PUT
Required Fields: eid, ename, esal, loc
Access Type: Public
'''
@emprouter.put("/{eid}")
def update_emp(eid: int, emp: EmployeeModel):
    emp_col.update_one({"eid": eid}, {"$set": emp.dict()})
    return {"msg": "Employee Updated Successfully"}


'''
usage: Delete Employee by Id
Rest API URL: http://127.0.0.1:8000/emp/101
Method Type: DELETE
Required Fields: None
Access Type: Public
'''
@emprouter.delete('/{eid}')
def delete_emp(eid: int):
    emp_col.delete_one({"eid": eid})
    return {"msg": "Employee Deleted Successfully"}
