from pydantic import BaseModel
from pydantic import EmailStr

from typing import Optional
from uuid import UUID


class User(BaseModel):
    id: Optional[UUID]
    name: str
    email: EmailStr
    
class UserCreated(BaseModel):
    message: str = "User is created"
    
class UserDeleted(BaseModel):
    message: str = "User deleted"
    
class UserUpdated(BaseModel):
    message: str = "User is updated"

class UserNotFound(BaseModel):
    message: str = "User is updated"
