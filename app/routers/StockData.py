from fastapi import APIRouter
from utils import pydanticModels
from typing import List


router = APIRouter(
  prefix = '/stockdata',
  tags = ['stockdata']
)


@router.post('/')
def getStockData(data:List[pydanticModels.StockPrices]):
  return {'data':data}

