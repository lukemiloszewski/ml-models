import base64
import json
import math
from typing import Dict

import cv2
import numpy as np

from ml_models.context import Context


def get_mnist_prediction(context: Context, input_data: str) -> Dict[str,str]:
    mnist_session = context.resources.mnist
    input_name = mnist_session.get_inputs()[0].name
    output_name = mnist_session.get_outputs()[0].name

    rv = _get_mnist_prediction(mnist_session, input_name, output_name, input_data)
    return rv


def _get_mnist_prediction(session, input_name: str, output_name: str, input_data: str) -> Dict[str,str]:
    preprocessed_data = _preprocess(input_data)
    prediction = _predict(session, input_name, output_name, preprocessed_data)
    return prediction


def _preprocess(input_data: str) -> Dict[str, list]:
    input_array = np.frombuffer(base64.b64decode(input_data), np.uint8)

    img = cv2.imdecode(input_array, cv2.IMREAD_COLOR)  # raw image

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale image
    img_blur = cv2.GaussianBlur(img_gray, (5,5), 0)  # blur image
    img_thresh = cv2.threshold(img_blur, 128, 255, cv2.THRESH_BINARY_INV)[1]  # threshold image

    x, y, w, h = cv2.boundingRect(img_thresh)  # bounding box
    img_box = img_thresh[y:y + h, x:x + w]

    rows, cols = img_box.shape
    if rows > cols:
        factor = 20/rows
        rows = 20
        cols = int(round(cols*factor))
    else:
        factor = 20/cols
        cols = 20
        rows = int(round(rows*factor))

    img_20_by_20 = cv2.resize(img_box, (cols, rows))  # 20x20 image

    cols_padding = (int(math.ceil((28-cols)/2)),int(math.floor((28-cols)/2)))
    rows_padding = (int(math.ceil((28-rows)/2)),int(math.floor((28-rows)/2)))

    img_28_by_28 = np.lib.pad(img_20_by_20,(rows_padding,cols_padding),'constant')  # 28x28 image
    img_28_by_28.resize((1, 1, 28, 28))

    output_data = json.dumps({"data": img_28_by_28.tolist()})
    return output_data


def _predict(session, input_name, output_name, input_data) -> Dict[str, str]:
    try:
        data = _preprocess_output(input_data)
        rv = session.run([output_name], {input_name: data})
        result = _postprocess(rv)
        result_dict = {"result": result}
    except Exception as e:
        result_dict = {"error": str(e)}

    return result_dict


def _preprocess_output(input_data):
    return np.array(json.loads(input_data)["data"]).astype("float32")


def _postprocess(output_data) -> int:
    return int(np.argmax(np.array(output_data).squeeze(), axis=0))
