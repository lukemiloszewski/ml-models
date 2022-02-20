import json

import numpy as np

from ml_models.context import Context


def predict_mnist(context: Context, input_data):
    mnist_session = context.resources.mnist
    input_name = mnist_session.get_inputs()[0].name
    output_name = mnist_session.get_outputs()[0].name

    result = _predict_mnist(mnist_session, input_name, output_name, input_data)
    return result


def _predict_mnist(session, input_name, output_name, input_data):
    try:
        data = _preprocess(input_data)
        rv = session.run([output_name], {input_name: data})
        result = _postprocess(rv)
        result_dict = {"result": result}
    except Exception as e:
        result_dict = {"error": str(e)}

    return result_dict


def _preprocess(input_data):
    return np.array(json.loads(input_data)["data"]).astype("float32")


def _postprocess(output_data):
    return int(np.argmax(np.array(output_data).squeeze(), axis=0))
