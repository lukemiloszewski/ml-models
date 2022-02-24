from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ml_models import __DESCRIPTION__, __TITLE__, __VERSION__
from ml_models.routers import health_router, mnist_router


_origins = [
    "http://localhost:3000",
    "localhost:3000"
]


def configure_app() -> FastAPI:
    app = FastAPI(
        title=f"{__TITLE__}",
        description=__DESCRIPTION__,
        version=__VERSION__,
        openapi_tags=[health_router.tag, mnist_router.tag],
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)

    app.include_router(health_router.router, prefix=health_router.prefix)
    app.include_router(mnist_router.router, prefix=mnist_router.prefix)
    return app
