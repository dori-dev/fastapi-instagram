from time import time

from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from router import user, article, file
from auth import authentication
from database.models import base
from database.db import create_all_models


app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(file.router)
app.include_router(authentication.router)

app.mount('/media', StaticFiles(directory='media'), name='files')

origins = [
    'https://127.0.0.1:3000',
    'https://127.0.0.1:8000',
    'https://www.google.com',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware('http')
async def add_middleware(request: Request, call_next):
    start_time = time()
    response: Response = await call_next(request)
    duration = time() - start_time
    response.headers['duration-time'] = f"{round(duration, 2)} ms"
    return response

create_all_models(base)
