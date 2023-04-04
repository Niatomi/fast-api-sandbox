from pydantic import BaseModel
from pydantic import EmailStr

from typing import Optional
from uuid import UUID

from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr
    
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str

class UserGet(UserBase):
    id: UUID
    is_email_confirmed: bool
    created_at: datetime
        
    class Config:
        orm_mode = True

    
class UserUpdate(UserBase):
    is_email_confirmed: bool
    
class UserCreated(BaseModel):
    message: str = "USER_IS_CREATED"
    
class UserDeleted(BaseModel):
    message: str = "USER_IS_DELETED"
    
class UserUpdated(BaseModel):
    message: str = "USER_IS_UPDATED"

class UserAlreadyExists(BaseModel):
    message: str = "USER_IS_ALREADY_EXISTS"

class UserNotFound(BaseModel):
    message: str = "USER_IS_NOT_FOUND"
