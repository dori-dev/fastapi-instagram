from os.path import exists as file_exists
import shutil

from fastapi import APIRouter, UploadFile, File, status, HTTPException
from fastapi.responses import FileResponse


router = APIRouter(prefix='/file', tags=['file'])


@router.post('/upload')
def upload_file(file: UploadFile = File(...)):
    name = file.filename
    type = file.content_type
    path = f'media/{name}'
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {
        'path': path,
        'type': type,
    }


@router.get('/download/{name}', response_class=FileResponse)
def download_file(name: str):
    path = f'media/{name}'
    if file_exists(path):
        return path
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='This file is not exists.',
    )
