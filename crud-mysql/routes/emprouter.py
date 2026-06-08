from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from config.database import get_db, init_db
from model.Employee import Employee, EmployeeSchema

# Create tables if they don't exist
init_db()

# Create API Router for Employee Operations
emprouter = APIRouter(prefix="/emp", tags=["Employee"])


'''
usage: Create Employee
Rest API URL: http://127.0.0.1:8000/emp/create
Method Type: POST
Required Fields: eid, ename, esal, loc
Access Type: Public
'''
@emprouter.post("/create")
def create_employee(emp: EmployeeSchema, db: Session = Depends(get_db)):
    # Check if employee with same eid already exists
    existing_emp = db.query(Employee).filter(Employee.eid == emp.eid).first()
    if existing_emp:
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    
    new_emp = Employee(eid=emp.eid, ename=emp.ename, esal=emp.esal, loc=emp.loc)
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return {"msg": "New Employee Created Successfully"}


'''
usage: Get all Employees
Rest API URL: http://127.0.0.1:8000/emp/read
Method Type: GET
Required Fields: None
Access Type: Public
'''
@emprouter.get("/read")
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees


'''
usage: Get Employee by id
Rest API URL: http://127.0.0.1:8000/emp/101
Method Type: GET
Required Fields: None
Access Type: Public
'''
@emprouter.get("/{eid}")
def get_emp_by_id(eid: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.eid == eid).first()
    
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
def update_emp(eid: int, emp: EmployeeSchema, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.eid == eid).first()
    
    if not employee:
        raise HTTPException(status_code=404, detail="Employee Not Found")
    
    employee.ename = emp.ename
    employee.esal = emp.esal
    employee.loc = emp.loc
    db.commit()
    db.refresh(employee)
    return {"msg": "Employee Updated Successfully"}


'''
usage: Delete Employee by Id
Rest API URL: http://127.0.0.1:8000/emp/101
Method Type: DELETE
Required Fields: None
Access Type: Public
'''
@emprouter.delete('/{eid}')
def delete_emp(eid: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.eid == eid).first()
    
    if not employee:
        raise HTTPException(status_code=404, detail="Employee Not Found")
    
    db.delete(employee)
    db.commit()
    return {"msg": "Employee Deleted Successfully"}
