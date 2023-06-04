from enum import Enum
from typing import Optional

from fastapi import APIRouter, status, Response

router = APIRouter(prefix='/blog', tags=['blog'])


class Types(str, Enum):
    T1 = 'type1'
    T2 = 'type2'
    T3 = 'type3'


@router.get('/{type}', status_code=status.HTTP_200_OK, tags=['hello'])
def hello(type: Types, page: Optional[int] = None, response: Response = None):
    if type == Types.T2:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            'msg': "The type is not valid"
        }
    return {
        'msg': f'Hello {type}!',
        'page': page,
    }
