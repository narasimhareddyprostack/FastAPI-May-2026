from fastapi import FastAPI
from routes.userrouter import router as user_router
from routes.productrouter import router as product_router
app=FastAPI()

'''
Usage: Application Root Request
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None
Access Type:None
'''
@app.get("/")
def index_page():
    return {"msg":"Application index Page"}


app.include_router(user_router)
app.include_router(product_router)