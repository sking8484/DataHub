from statistics import mode
from fastapi import APIRouter, Depends, HTTPException
from utils import pydanticModels
from typing import List
from utils.db.database import get_db, engine, get_raw_db
from sqlalchemy.sql.expression import func
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


@router.get('/')
def getStockData(db:Session = Depends(get_raw_db)):
  SQL = f'SELECT * FROM {models.StockPricing.__tablename__}'
  cursor = db[0]
  cursor.execute(SQL)
  data = cursor.fetchall()
  return data

#base/maxcol/symbol
@router.get('/{column}/{symbol}')
def getMaxDate(column:str, symbol:str,db:Session = Depends(get_raw_db)):

  SQL = f'SELECT MAX({column}) FROM {models.StockPricing.__tablename__} WHERE SYMBOL = %s'
  db[0].execute(SQL, [symbol])
  data = db[0].fetchone()
  return data[f'MAX({column})']
