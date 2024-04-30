from typing import Union
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from .routes import devices_router
from .config import SQLALCHEMY_DATABASE_URL

def connect_db():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    if not database_exists(engine.url):
        create_database(engine.url)

connect_db()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(devices_router)