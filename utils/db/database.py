from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import settings


SQLALCHEMY_DATABASE_URL = f'mysql+mysqlconnector://{settings.database_user}:{settings.database_password}@{settings.database_host}/{settings.database}'

engine = create_engine(
  SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()