from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date

from sqlalchemy.orm import relationship

from .database import Base

class StockPricing(Base):
  __tablename__ = 'sp100Prices'

  date = Column(Date, primary_key = True)
  symbol = Column(String(252), primary_key = True)
  value = Column(Float, primary_key = True)
