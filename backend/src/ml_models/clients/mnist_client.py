import base64
import math

import cv2
import numpy as np
import onnxruntime


class MNISTClient:
    def __init__(self, path: str):
        self.path = path
        self.session = onnxruntime.InferenceSession(self.path)
        self.input_name = self.session.get_inputs()[0].name
        self.output_name = self.session.get_outputs()[0].name

    def predict(self, input_data: np.ndarray) -> int:
        preprocessed_data = self._preprocess(input_data)
        prediction = self._predict(preprocessed_data)
        postprocessed_data = self._postprocess(prediction)
        return postprocessed_data

    def _preprocess(self, input_data: str) -> np.ndarray:
        input_array = np.frombuffer(base64.b64decode(input_data), np.uint8)

        img = cv2.imdecode(input_array, cv2.IMREAD_COLOR)  # raw image

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale image
        img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)  # blur image
        img_thresh = cv2.threshold(img_blur, 128, 255, cv2.THRESH_BINARY_INV)[
            1
        ]  # threshold image

        x, y, w, h = cv2.boundingRect(img_thresh)  # bounding box
        img_box = img_thresh[y : y + h, x : x + w]

        rows, cols = img_box.shape
        if rows > cols:
            factor = 20 / rows
            rows = 20
            cols = int(round(cols * factor))
        else:
            factor = 20 / cols
            cols = 20
            rows = int(round(rows * factor))

        img_20_by_20 = cv2.resize(img_box, (cols, rows))  # 20x20 image

        cols_pad = (int(math.ceil((28 - cols) / 2)), int(math.floor((28 - cols) / 2)))
        rows_pad = (int(math.ceil((28 - rows) / 2)), int(math.floor((28 - rows) / 2)))

        img_28_by_28 = np.lib.pad(
            img_20_by_20, (rows_pad, cols_pad), "constant"
        )  # 28x28 image
        img_28_by_28.resize((1, 1, 28, 28))

        preprocessed_data = img_28_by_28.astype("float32")
        return preprocessed_data

    def _predict(self, preprocessed_data: np.ndarray) -> np.ndarray:
        prediction = self.session.run([self.output_name], {self.input_name: preprocessed_data})
        return prediction

    def _postprocess(self, prediction: np.ndarray) -> int:
        postprocessed_data = int(np.argmax(np.array(prediction).squeeze(), axis=0))
        return postprocessed_data
