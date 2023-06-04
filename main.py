from fastapi import FastAPI

from router import user
from database.models import base
from database.db import create_all_models


app = FastAPI()
app.include_router(user.router)

create_all_models(base)
