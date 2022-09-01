from fastapi import FastAPI
from .routers import StockData

app = FastAPI()
app.include_router(StockData.router)

@app.get("/")
def root():
  return {'Message':"Welcoome to DataHub"}