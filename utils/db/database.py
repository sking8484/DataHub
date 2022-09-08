from curses import echo
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from ..config import settings
import mysql.connector




SQLALCHEMY_DATABASE_URL = f'mysql+mysqlconnector://{settings.database_user}:{settings.database_password}@{settings.database_host}/{settings.database}'

engine = create_engine(
  SQLALCHEMY_DATABASE_URL, echo=False
)

SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=engine)

Base = declarative_base()



def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


def get_raw_db():
  cnxn = mysql.connector.connect(user = settings.database_user, password = settings.database_password, host = settings.database_host, database = settings.database)

  cursor = cnxn.cursor(dictionary=True)
  try:
    yield [cursor, cnxn]
  finally:
    cnxn.close()