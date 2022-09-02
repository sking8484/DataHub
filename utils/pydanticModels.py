from pydantic import BaseModel
from datetime import date, datetime, time, timedelta
from typing import List


class StockPrices(BaseModel):
  date: str
  symbol: str
  value: str



class StockPricesOut(StockPrices):

  class Config:
    orm_mode = True

