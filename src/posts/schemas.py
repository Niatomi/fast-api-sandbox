from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

from users.schemas import UserGet

class PostBase(BaseModel):
    title: str
    content: str
    is_published: bool
    
    class Config:
        orm_mode = True
        
class PostCreate(PostBase):
    owner_id: UUID
    created_at: datetime = datetime.now()
    
class PostAll(PostBase):        
    id: UUID
    created_at: datetime = datetime.now()
    owner: Optional[UserGet]
    
    class Config:
        orm_mode = True
        
class PostCreated(BaseModel):
    message: str = "POST_IS_CREATED"
    
class PostDeleted(BaseModel):
    message: str = "POST_IS_CREATED"
    
class PostUpdated(BaseModel):
    message: str = "POST_IS_UPDATED"
    
class PostNotFound(BaseModel):
    message: str = "POST_IS_NOT_FOUND"
    
class PostChangeNotAllowed(BaseModel):
    message: str = "CURRENT_POST_IS_NOT_OF_THIS_USER"
    