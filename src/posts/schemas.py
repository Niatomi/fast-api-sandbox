from pydantic import BaseModel

class PostCreated(BaseModel):
    message: str = "POST_IS_CREATED"
    
class PostUpdated(BaseModel):
    message: str = "POST_IS_UPDATED"
    
class PostNotFound(BaseModel):
    message: str = "POST_IS_NOT_FOUND"
    