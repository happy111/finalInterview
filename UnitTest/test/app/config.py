from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Database settings
    database_url: str = "mysql+pymysql://root:password@localhost:3306/fastapi_crud"
    db_host: str = "localhost"
    db_port: int = 3306
    db_user: str = "root"
    db_password: str = "password"
    db_name: str = "fastapi_crud"
    
    # JWT settings
    secret_key: str = "your-secret-key-here-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Application settings
    environment: str = "development"
    debug: bool = True
    
    class Config:
        env_file = "config.env"
        case_sensitive = False


settings = Settings() 