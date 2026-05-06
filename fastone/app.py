from fastapi import FastAPI
#create FastAPI app
app = FastAPI()

'''
Usage: Application Root
Rest API URL:http://127.0.0.1:8000/
Method Type:GET
Required Fields:None
Access Type:Public
'''
@app.get("/")
def index_page():
    return {"message":"Index Page"}

'''
Usage: About Page
Rest API URL:http://127.0.0.1:8000/about
Method Type:GET
Required Fields:None
Access Type:Public
'''
@app.get("/about")
def about_page():
    return {"message":"About Page"}
