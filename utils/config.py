from pydantic import BaseSettings


class Settings(BaseSettings):
  database_host: str
  database_user: str
  database_password: str
  database: str

  class Config:
    env_file = '.env'


settings = Settings()