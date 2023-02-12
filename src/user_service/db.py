from models import Gender, Role, User
from models.dto import UserDto
from models.errors import BadRequestException

from uuid import UUID, uuid4 as uuid 
from loguru import logger as log

_users = [
    User(
        id=UUID('4dce9d3e-8be3-49b6-a6b9-7a32a8638246'),
        first_name="Adam",
        second_name="Luke",
        third_name="Pale",
        gender=Gender.male,
        role=Role.student
    ),
    User(
        id=UUID('4dce9d3e-8be3-49b6-a6b9-7a32a8638247'),
        first_name="Jinx",
        second_name="The",
        third_name="cat",
        gender=Gender.male,
        role=Role.admin
    ),
    User(
        id=UUID('4dce9d3e-8be3-49b6-a6b9-7a32a8638248'),
        first_name="Paul",
        second_name="Gilbert",
        third_name=None,
        gender=Gender.male,
        role=Role.student
    ),
    
]

def get_all_users():
    return _users

def add_new_user(user: User):
    _users.append(user)
    
def delete_user_by_uuid(id: UUID):
    id = UUID(id)
    for u in _users:
        if u.id == id:
            _users.remove(u)
            return True
    raise BadRequestException()

def delete_user_by_name(name: str):
    for u in _users:
        if u.first_name == name:
            _users.remove(u)
            return True
    raise BadRequestException()
            
def update_user_by_uuid(id: str, new_info: UserDto):
    id = UUID(id)
    for u in _users:
        if u.id == id:
            for param in new_info:
                if param == None:
                    new_info[param] == u[param]
            _users.remove(u)
            _users.append(new_info)
            return True
    raise BadRequestException()
            