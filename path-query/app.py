from fastapi import FastAPI
from routes.productRouter import router
app=FastAPI()


'''
usage:Application Root Request
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
'''
@app.get("/")
def application_root():
    return {"msg":"Application root"}


#forward all product Path request to -productRouter file
app.include_router(router)