from fastapi import FastAPI

from router import home, test


app = FastAPI()
app.include_router(home.router)
app.include_router(test.router)
