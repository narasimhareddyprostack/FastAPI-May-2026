from fastapi import FastAPI

app=FastAPI()

'''
Usage:
Rest API URL: http://127.0.0.1:8000/api/user/update
Method Type:PUT
Required Fields: None
Access Type: Public
'''
@app.put("/api/user/update")
def updateuser():
    return {"msg":"User Updated Successfully"}


'''
Usage:delete user
Rest API URL: http://127.0.0.1:8000/d2/d3/d4
Method Type:DELETE
Required Fields: None
Access Type: Public
'''
@app.delete("/d2/d3/d4/")
def deluser():
    return {"msg":"user Delelted"}


#uvicorn server:app --reload