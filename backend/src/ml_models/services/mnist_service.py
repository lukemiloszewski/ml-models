from ml_models.clients.mnist_client import MNISTClient
from ml_models.context import Context


def get_mnist_prediction(context: Context, input_data: str) -> int:
    mnist_client = context.clients.get("mnist")
    prediction = _get_mnist_prediction(mnist_client, input_data)
    return prediction


def _get_mnist_prediction(mnist_client: MNISTClient, input_data: str) -> int:
    rv = mnist_client.predict(input_data)
    return rv
