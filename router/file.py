from string import ascii_letters
from random import choices
from os.path import exists as file_exists
import shutil

from fastapi import APIRouter, UploadFile, File, status, HTTPException
from fastapi.responses import FileResponse


router = APIRouter(prefix='/file', tags=['file'])


def generate_name(file: UploadFile) -> str:
    random_name = "".join(choices(ascii_letters, k=10))
    extension = file.filename.rsplit('.', 1)[1]
    name = f"{random_name}.{extension}"
    return f'media/{name}'


@router.post('/upload')
def upload_file(file: UploadFile = File(...)):
    path = generate_name(file)
    while file_exists(path):
        path = generate_name(file)
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {
        'file_path': path,
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
