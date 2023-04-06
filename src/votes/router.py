from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from auth.oauth2 import get_current_user

from votes import schemas

from models import User

from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from repository.votes import VoteCrud
from repository.posts import PostsCrud 
from votes.exceptions import VoteException
from posts.exceptions import PostNotFoundException

router = APIRouter(
    prefix='/votes',
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "User is not logged in"
        }
    },
    dependencies=[Depends(get_current_user)]
)

@router.post("/",
             responses={
                 status.HTTP_200_OK: {
                     "model": schemas.VoteCreated,
                     "description": "User vote applied"
                 },
                 status.HTTP_204_NO_CONTENT: {
                     "description": "User vote removed"
                 },
                 status.HTTP_405_METHOD_NOT_ALLOWED: {
                     "model": schemas.VoteExceptionResponse,
                     "description": "User applied vote choise twice or more"
                 }
             })
async def vote(vote_dir: schemas.VoteEnum,
               post: schemas.PostInfo,
               session: AsyncSession = Depends(get_async_session),
               user: User = Depends(get_current_user)):
    
    if await PostsCrud.get_by_id(session=session, id=post.post_id) is None:
        raise PostNotFoundException
    
    vote = schemas.Vote(post_id=post.post_id,
                    user_id=user.id)
    result = await VoteCrud.get_by_body(session=session, vote=vote)
    
    if vote_dir is schemas.VoteEnum.vote:
        if result is not None:
            raise VoteException
        
        await VoteCrud.create(session=session, vote=vote)
        return schemas.VoteCreated()
    if vote_dir is schemas.VoteEnum.unvote:
        if result is None:
            raise VoteException
        
        await VoteCrud.delete(session=session, vote=vote)
        return Response(status_code=status.HTTP_204_NO_CONTENT)