from fastapi import Request, status
from fastapi.responses import JSONResponse, Response

from src.main import app


@app.exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR)
async def server_exception_handler(_request: Request, _exc: Exception) -> Response:
    return JSONResponse({'error': 'Server Error (500)'}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
