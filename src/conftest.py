from fastapi import FastAPI

import pytest
import sentry_sdk
from httpx2 import ASGITransport, AsyncClient

import logging
from collections.abc import AsyncGenerator


@pytest.fixture(scope='session', autouse=True)
def app() -> FastAPI:
    from src.main import app

    logging.disable(logging.CRITICAL)
    sentry_sdk.init(dsn='')  # disable events capturing
    return app


@pytest.fixture(scope='session')
async def client(app) -> AsyncGenerator[AsyncClient]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://testserver') as client:
        yield client
