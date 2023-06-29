from fastapi import FastAPI

from router import user, article
from database.models import base
from database.db import create_all_models


app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)

create_all_models(base)


# @app.exception_handler(EmailNotValid)
# def email_not_valid(request: Request, exc: EmailNotValid):
#     return JSONResponse(
#         content=str(exc),
#         status_code=status.HTTP_400_BAD_REQUEST
#     )
