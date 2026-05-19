from fastapi import FastAPI
from routes.emprouter import emprouter


#create FastAPI app and Root Request API
app = FastAPI()

# Include Employee Router
app.include_router(emprouter)


'''
usage: Application Root
Rest API URL: http://127.0.0.1:8000/
Method Type: GET
Required Fields: None
Access Type: Public
'''
@app.get("/")
def application_root_req():
    return {"msg": "Application Root"}

