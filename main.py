from fastapi import FastAPI

from router import home, test
from database.models import base
from database.db import create_all_models


app = FastAPI()
app.include_router(home.router)
app.include_router(test.router)

create_all_models(base)
