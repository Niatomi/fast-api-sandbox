from pydantic import BaseModel
from pydantic import EmailStr

class UserCredentials(BaseModel):
    email: EmailStr
    password: str
    
class WrongCredentials(BaseModel):
    message: str = "INVALID_CREDENTIALS"
    
class UserToken(BaseModel):
    access_token: str = "ACTUAL_TOKEN"
    token_type: str = "Bearer"
    
class TokenData(BaseModel):
    id: str