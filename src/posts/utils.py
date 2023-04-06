from fastapi import Depends
from database import get_async_session
from repository.posts import PostsCrud
from models import User
from sqlalchemy.ext.asyncio import AsyncSession
from posts.exceptions import NotAllowedException
from uuid import UUID
from auth.oauth2 import get_current_user

async def check_user_own(id: UUID, session: AsyncSession = Depends(get_async_session), user: User = Depends(get_current_user)):
    post = await PostsCrud.get_by_id(session=session, id=id)
    if post.owner_id != user.id:
        raise NotAllowedException