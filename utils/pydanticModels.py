from pydantic import BaseModel
from datetime import date, datetime, time, timedelta


class StockPrices(BaseModel):
  date: date
  symbol: str
  price: float


