from fastapi import UploadFile, APIRouter, Response
from http import HTTPStatus

router = APIRouter(prefix='/clinet')

@router.get('/list_of_workers')
async def get_workers():
    return Response(status_code=HTTPStatus.OK)
