from pydantic import BaseModel
from datetime import date, time, timedelta
from typing import List


class StockPrices(BaseModel):
  date: str
  symbol: str
  value: float

class StockPricesOut(StockPrices):

  class Config:
    orm_mode = True

