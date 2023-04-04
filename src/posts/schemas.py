from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    is_published: bool
    
    class Config:
        orm_mode = True

class PostAll(PostBase):        
    id: UUID
    created_at: datetime
    
    class Config:
        orm_mode = True

class PostUpdate(PostBase):
    pass

class PostCreated(BaseModel):
    message: str = "POST_IS_CREATED"
    
class PostDeleted(BaseModel):
    message: str = "POST_IS_CREATED"
    
class PostUpdated(BaseModel):
    message: str = "POST_IS_UPDATED"
    
class PostNotFound(BaseModel):
    message: str = "POST_IS_NOT_FOUND"
    