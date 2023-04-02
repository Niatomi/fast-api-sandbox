from typing import Union
from fastapi import FastAPI, Response, status, Request
from fastapi.responses import JSONResponse

from models.dto import UserDto
from models.errors import BadRequestException
import user_service as service

app = FastAPI()

@app.exception_handler(BadRequestException)
async def unicorn_exception_handler(request: Request, exc: BadRequestException):
    return JSONResponse(
        status_code=400,
        content={"message": f"{exc.name}"},
    )
    
@app.exception_handler(ValueError)
async def unicorn_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"message": f"{exc}"},
    )

@app.get("/users")
async def get_all_users():
    return service.get_all_users()

@app.put("/add")
async def add_new_user(user: UserDto):
    service.add_new_user(user)
    return "User added"
    
@app.delete("/deleteUser")
async def delete_user_by_name(name: str, response: Response):
    res = service.delete_user_by_name(name)
    return "User deleted"
        
@app.delete("/deleteUserByUUID")
async def delete_user_by_name(UUID: str, response: Response):
    res = service.delete_user_by_uuid(UUID)
    return "User deleted"
        
@app.patch("/updateUser")
async def update_user(uuid: str, updated_user: UserDto, response: Response):
    res = service.update_user_by_uuid(uuid, updated_user)
    return "User updated"
