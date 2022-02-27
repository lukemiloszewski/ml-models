import pathlib

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

config = Config(".env")


ROOT_PATH = config("ROOT_PATH", default=pathlib.Path(__file__).parent)
MNIST_ONNX_PATH = config("MNIST_ONNX_PATH", default="data/mnist.onnx")
CORS_ORIGINS = config("CORS_ORIGINS", default=["http://localhost:3000", "localhost:3000"], cast=CommaSeparatedStrings)
