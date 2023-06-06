from fastapi import FastAPI

from router import user, article
from database.models import base
from database.db import create_all_models


app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)

create_all_models(base)
