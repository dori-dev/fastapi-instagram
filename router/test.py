from typing import Optional, List, Dict
from pydantic import BaseModel

from fastapi import APIRouter, Query, Body, Path


router = APIRouter(prefix='/blog', tags=['blog'])


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    comment: int
    published: Optional[bool]
    tags: List[str]
    metadata: Dict[str, str] = {'key1': 'value1'}
    image: Image = None


@router.post('/new/{id}')
def create_blog(
        blog: BlogModel,
        id: int,
        content: str =
        Body(...,
             min_length=10,
             max_length=30,
             regex='^a.*5',
             ),
        version: int =
        Query(
            None,
            alias='v',
        ),
        lst: Optional[List[str]] = Query(None),
):
    return {
        "id": id,
        "version": version,
        "data": blog,
        "content": content,
    }
