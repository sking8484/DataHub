from pydantic import BaseModel
from datetime import date, datetime, time, timedelta
from typing import List


class StockPrices(BaseModel):
  date: datetime
  symbol: str
  value: float



class StockPricesOut(StockPrices):

  class Config:
    orm_mode = True

