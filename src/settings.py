import pydantic
from pydantic_settings import BaseSettings, SettingsConfigDict

from pathlib import Path
from typing import ClassVar


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='APP_', case_sensitive=True)

    BASE_DIR: ClassVar[Path] = Path(__file__).resolve().parent.parent

    ENV: str = 'dev'

    SECRET_KEY: pydantic.SecretStr = pydantic.SecretStr('d283cf4fb4ca8b1aeec08a5eaa8f0bb4')

    DEBUG: bool = False

    # Application definition

    TEMPLATES_DIR: ClassVar[Path] = BASE_DIR / 'templates'

    # Feature vars

    FEATURE_SWAGGER: bool = True

    FEATURE_SENTRY: bool = True

    # REST API

    SWAGGER_TITLE: ClassVar[str] = 'Template API'
    SWAGGER_VERSION: ClassVar[str] = 'v1'
    SWAGGER_SEPARATE_INPUT_OUTPUT_SCHEMAS: ClassVar[bool] = True
    SWAGGER_UI_SETTINGS: ClassVar[dict] = {
        'deepLinking': True,
        'displayRequestDuration': True,
        'persistAuthorization': True,
    }

    # Logging

    LOGGING: ClassVar[dict] = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                '()': 'logging.StreamHandler',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'loggers': {
            'uvicorn.error': {
                'handlers': ['console'],
                'propagate': False,
            },
            'httpx2': {
                'level': 'WARNING',
            },
        },
    }

    # Static files (CSS, JavaScript, Images)

    STATIC_URL: ClassVar[str] = '/static'

    # Sentry

    SENTRY_DSN: str = ''
    SENTRY_SAMPLE_RATE: float = 0.5


settings = Settings()
