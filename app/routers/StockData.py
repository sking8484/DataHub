from fastapi import APIRouter, Depends, HTTPException
from utils import pydanticModels
from typing import List
from utils.db.database import get_db, engine, get_raw_db
from sqlalchemy.orm import Session
from utils.db import models
import json

router = APIRouter(
  prefix = '/stockdata',
  tags = ['stockdata']
)

#, db: Session = Depends(get_db)
@router.post('/')
def postStockData(data:List[pydanticModels.StockPrices], raw_db = Depends(get_raw_db)):

  cursor = raw_db[0]
  cnxn = raw_db[1]

  # i = 0
  # for row in data:
  #   if i % 10 == 0:
  #     print(i)
  #     db.flush()
  #   i += 1
  #   db_pricing = models.StockPricing(**row.dict())
  #   db.add(db_pricing)
  # db.commit()
  SQL = "INSERT INTO " + models.StockPricing.__tablename__ + " (date, symbol, value) VALUES"

  dataToInsert = []
  for row in data:
    row = row.dict()
    dataToInsert.append(row['date'])
    dataToInsert.append(row['symbol'])
    dataToInsert.append(row['value'])
    SQL += '(%s, %s, %s),'







  cursor.execute(SQL[:-1], dataToInsert)
  cnxn.commit()



  return {'message':'Pricing Updated'}

@router.get('/', response_model=List[pydanticModels.StockPricesOut])
def getStockData(db:Session = Depends(get_db)):
  return db.query(models.StockPricing).all()