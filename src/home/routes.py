from fastapi import APIRouter

router = APIRouter(tags=['resource'])


@router.get('/resource/{code}/', summary='Retrieve a resource')
async def resource_retrieve(code: str):
    return {'code': code}
