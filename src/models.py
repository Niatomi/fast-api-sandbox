from database import Base

from sqlalchemy import (
    Column,
    String,
    Boolean,
    Date
)
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4 as uuid
from datetime import datetime

class User(Base):
    __tablename__ = "user_table"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid)


class Post(Base):
    __tablename__ = "posts_table"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    is_published = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)