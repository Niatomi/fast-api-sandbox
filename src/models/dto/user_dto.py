from pydantic import BaseModel
from ..gender import Gender
from ..role import Role

class UserDto(BaseModel):
    first_name: str = None
    second_name: str = None
    third_name: str = None
    gender: Gender = Gender.male
    role: Role = None