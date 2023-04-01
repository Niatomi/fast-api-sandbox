from pydantic import BaseModel

from uuid import UUID
from uuid import uuid4 as uuid
from .gender import Gender
from .role import Role

class User(BaseModel):
    id: UUID = uuid()
    first_name: str = None
    second_name: str = None
    third_name: str = None
    gender: Gender = Gender.male
    role: Role = Role.student