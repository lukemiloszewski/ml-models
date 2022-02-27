from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ml_models import __DESCRIPTION__, __TITLE__, __VERSION__
from ml_models.logging import log_request_metadata
from ml_models.routers import health_router, mnist_router


def configure_app(cors_origins: List[str]) -> FastAPI:
    app = FastAPI(
        title=f"{__TITLE__}",
        description=__DESCRIPTION__,
        version=__VERSION__,
        openapi_tags=[health_router.tag, mnist_router.tag],
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health_router.router, prefix=health_router.prefix)
    app.include_router(mnist_router.router, prefix=mnist_router.prefix)

    request_middleware = app.middleware("http")
    request_middleware(log_request_metadata)

    return app
