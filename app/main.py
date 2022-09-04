from fastapi import FastAPI, Depends, HTTPException
from .routers import StockData
from utils.db.database import SessionLocal, engine, get_db
from utils import pydanticModels
from utils.db import models
from starlette.datastructures import UploadFile as StarletteUploadFile
from fastapi.middleware.cors import CORSMiddleware




# keep the SpooledTemporaryFile in-memory
StarletteUploadFile.spool_max_size = 0
models.Base.metadata.create_all(bind = engine)


app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(StockData.router)

@app.get("/")
def root():
  return {'Message':"Welcoome to DataHub"}