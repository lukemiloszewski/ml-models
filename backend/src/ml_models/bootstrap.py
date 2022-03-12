from fastapi import FastAPI

from ml_models.app import configure_app
from ml_models.context import configure_context
from ml_models.logging import configure_logging


def create_app(config) -> FastAPI:
    configure_logging(logs_path=config.LOGS_PATH)
    configure_context(root_path=config.ROOT_PATH, mnist_onnx_path=config.MNIST_ONNX_PATH)

    app = configure_app(cors_origins=config.CORS_ORIGINS)
    return app
