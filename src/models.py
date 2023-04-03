from database import Base

from sqlalchemy import (
    Column,
    String,
    Boolean
)
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4 as uuid
from datetime import datetime

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_table"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid)
    name = Column(String, nullable=False)
    login = Column(String, unique=True, nullable=False)
    is_email_confirmed = Column(String, nullable=False)
    

class Post(Base):
    __tablename__ = "posts_table"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    is_published = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)