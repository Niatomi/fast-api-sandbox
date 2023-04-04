from pydantic import BaseModel
from pydantic import EmailStr

class UserCredentials(BaseModel):
    email: EmailStr
    password: str
    
class WrongCredentials(BaseModel):
    message: str = "INVALID_CREDENTIALS"
    
class UserToken(BaseModel):
    token: str = "ACTUAL_TOKEN"