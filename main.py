# main.py
# Import FastAPI
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import api
from database import db_engine
from models import CarInfo

# Initialize the app
app = FastAPI()

app.include_router(api.router)

# CarInfo.Base.metadata.create_all(db_engine.engine)

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to Balasundar's Technical Blog"}
