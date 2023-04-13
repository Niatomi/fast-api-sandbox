from pydantic import BaseSettings

class TestConfig(BaseSettings):
    db_host: str = 'localhost'
    db_user: str = 'postgres'
    db_pass: str = 'postgres'
    db_port: int = 5431
    db_name: str = 'posts_database_test'

    secret: str = 'iyvbwrevbierwbvierubviuerbviurebvui'
    algorithm: str = 'HS256'
    access_token_expiry: int = 60
    
test_config = TestConfig()