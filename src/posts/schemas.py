from pydantic import BaseModel

class PostCreated(BaseModel):
    message: str = "Post is created"
    
class PostUpdated(BaseModel):
    message: str = "Post is updadated"
    
class PostNotFound(BaseModel):
    message: str = "Post is not found"
    