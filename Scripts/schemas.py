from pydantic import BaseModel

from typing import Optional

class Post(BaseModel):
    id: Optional[int]
    title: str  
    content: str
    is_published: Optional[bool] = False
    