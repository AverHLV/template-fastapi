from fastapi import FastAPI

import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration

import re
from logging.config import dictConfig

from src.settings import settings

dictConfig(settings.LOGGING)

if settings.FEATURE_SENTRY:
    sentry_sampler_exclude_regex = re.compile(rf'(/liveness|/readiness|{settings.STATIC_URL})')

    def sentry_traces_sampler(context: dict) -> float:
        """Determine sample rate based on transaction context."""

        path_info = context.get('asgi_scope', {}).get('path')
        if not path_info:
            path_info = context.get('wsgi_environ', {}).get('PATH_INFO')
        if path_info and re.match(sentry_sampler_exclude_regex, path_info):
            return 0
        return settings.SENTRY_SAMPLE_RATE

    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        environment=settings.ENV,
        send_default_pii=True,
        traces_sampler=sentry_traces_sampler,
        integrations=[
            FastApiIntegration(),
        ],
    )
else:
    sentry_sdk.init(dsn='')

app = FastAPI(
    debug=settings.DEBUG,
    title=settings.SWAGGER_TITLE,
    version=settings.SWAGGER_VERSION,
    docs_url='/api/docs/' if settings.FEATURE_SWAGGER else None,
    openapi_url='/api/docs/schema/' if settings.FEATURE_SWAGGER else None,
    swagger_ui_parameters=settings.SWAGGER_UI_SETTINGS,
    separate_input_output_schemas=settings.SWAGGER_SEPARATE_INPUT_OUTPUT_SCHEMAS,
    redoc_url=None,
)


# include exception handlers, middleware, routers

from src import exception_handlers, home, middleware  # noqa: E402, F401

app.include_router(home.router, prefix='/api')
