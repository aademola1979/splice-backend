from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "To do"

    #class Config:
        #env_file = ".env"