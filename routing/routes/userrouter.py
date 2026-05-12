from fastapi import APIRouter

router=APIRouter(prefix='/user')

'''
Usage: User Router Request
Rest API URL: http://127.0.0.1:8000/user
Method Type:GET
Required Fields: None
Access Type:None
'''

@router.get("/")
def getusers():
    return {"msg":"Fetching all users"}



'''
Usage: create new user
Rest API URL: http://127.0.0.1:8000/user/create
Method Type:POST
Required Fields: uid,uname,loc,gender
Access Type:None
'''
@router.post("/create")
def create_user():
    return {"msg":"User Created Succesfully"}
