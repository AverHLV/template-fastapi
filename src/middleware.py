from fastapi import Request
from fastapi.responses import PlainTextResponse

from src.main import app


async def liveness() -> PlainTextResponse:
    return PlainTextResponse('OK')


async def readiness() -> PlainTextResponse:
    return PlainTextResponse('OK')


@app.middleware('http')
async def health_check_middleware(request: Request, call_next):
    """Middleware that provides check endpoints for k8s."""

    match request.url.path.rstrip('/'):
        case '/liveness':
            return await liveness()
        case '/readiness':
            return await readiness()
        case _:
            return await call_next(request)
