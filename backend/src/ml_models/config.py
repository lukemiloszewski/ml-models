from pathlib import Path

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

config = Config(".env")


ROOT_PATH = config("ROOT_PATH", default=Path(__file__).parent, cast=Path)
LOGS_PATH = config("LOGS_PATH", default=Path("logs/logs.log"), cast=Path)
MNIST_ONNX_PATH = config("MNIST_ONNX_PATH", default=Path("data/mnist.onnx"), cast=Path)
CORS_ORIGINS = config("CORS_ORIGINS", default=["http://localhost:3000", "localhost:3000"], cast=CommaSeparatedStrings)
