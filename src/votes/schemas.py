from pydantic import BaseModel

from enum import Enum
from uuid import UUID


class VoteEnum(str, Enum):
    vote = 'vote'
    unvote = 'unvote'

class PostInfo(BaseModel):
    post_id: UUID
    
class Vote(PostInfo):
    user_id: UUID
    
class VoteCreated(BaseModel):
    message: str = 'VOTE_ACCEPTED'
    
class VoteDeleted(BaseModel):
    message: str = 'VOTE_REMOVED'
    
class VoteExceptionResponse(BaseModel):
    message: str = 'CANNOT_APPLY_VOTE'
    

    
