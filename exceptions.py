from fastapi.exceptions import HTTPException
from fastapi import status


class EmailNotValid(HTTPException):
    def __init__(self, detail):
        super().__init__(status.HTTP_400_BAD_REQUEST, detail)
