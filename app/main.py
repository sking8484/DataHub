from fastapi import FastAPI, Depends, HTTPException
from .routers import StockData
from utils.db.database import SessionLocal, engine, get_db
from utils import pydanticModels
from utils.db import models

models.Base.metadata.create_all(bind = engine)


app = FastAPI()
app.include_router(StockData.router)

@app.get("/")
def root():
  return {'Message':"Welcoome to DataHub"}