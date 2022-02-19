from fastapi import FastAPI

from ml_models.app import configure_app
from ml_models.context import configure_context
from ml_models.logging import configure_logging


def create_app() -> FastAPI:
    configure_logging()
    configure_context()

    app = configure_app()
    return app
