import shutil
from fastapi import APIRouter, UploadFile, File


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
