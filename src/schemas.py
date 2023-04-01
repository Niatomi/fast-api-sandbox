from pydantic import BaseModel
from uuid import uuid4
from typing import Optional

class Post(BaseModel):
    id: Optional[str] 
    title: str  
    content: str
    is_published: Optional[bool] = False
    