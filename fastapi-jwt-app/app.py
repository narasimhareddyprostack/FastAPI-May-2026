from fastapi import FastAPI

from database.db import engine,Base
from routes.auth_router import router as auth_router
from routes.user_router import router as user_router

#if table's not exist, create Database table
Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/")
def index_page():
    return {"msg":"Application Root"}

#forward all user module API to auth_router & user_router
app.include_router(auth_router)
app.include_router(user_router)