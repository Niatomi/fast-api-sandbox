from pydantic import BaseSettings
from pydantic import Pyda


class Config(BaseSettings):
    db_host: str = 'localhost'
    db_user: str = 'postgres'
    db_pass: str = 'postgres'
    db_port: str =  '5430'
    db_name: str

    secret: str
    algorithm: str = 'HS256'
    access_token_expiry: int = 60
    
    class Config:
        if __name__ == "src.config":
            env_file = ".env"
        else:
            env_file = "../.env"
        env_file_encoding = 'utf-8'
    
config = Config()