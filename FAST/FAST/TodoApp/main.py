from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
import models
from models import Todos
from database import engine, SessionLocal

app=FastAPI()


models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""yield basically means return"""
"""this means we can contact the data base"""

db_dependency=Annotated[Session, Depends(get_db)]

@app.get("/")
async def read_all(db:db_dependency):
    return db.query(Todos).all()
"""Depends is dependency injection which means we have to do something before
what we trying to execute"""
