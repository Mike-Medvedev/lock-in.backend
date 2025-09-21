
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
    STRIPE_KEY: str

   

settings = Settings()