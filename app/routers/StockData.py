from fastapi import APIRouter, Depends, HTTPException
from utils import pydanticModels
from typing import List
from utils.db.database import get_db
from sqlalchemy.orm import Session
from utils.db import models

router = APIRouter(
  prefix = '/stockdata',
  tags = ['stockdata']
)


@router.post('/')
def postStockData(data:List[pydanticModels.StockPrices], db: Session = Depends(get_db)):
  for row in data:
    db_pricing = models.StockPricing(**row.dict())
    db.add(db_pricing)

  db.commit()
  return {'message':'Pricing Updated'}

@router.get('/', response_model=List[pydanticModels.StockPricesOut])
def getStockData(db:Session = Depends(get_db)):
  return db.query(models.StockPricing).all()