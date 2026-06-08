from fastapi import FastAPI
from routes.emprouter import emprouter
from config.database import init_db


#create FastAPI app and Root Request API
app = FastAPI()

# Initialize database (create tables)
init_db()

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

