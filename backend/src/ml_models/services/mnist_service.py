import base64
import json
import math

import cv2
import numpy as np
from scipy import ndimage

from ml_models.context import Context


def get_mnist_prediction(context: Context, data: str):
    mnist_session = context.resources.mnist
    input_name = mnist_session.get_inputs()[0].name
    output_name = mnist_session.get_outputs()[0].name

    preprocessed_data = preprocess(data)
    prediction = predict(mnist_session, input_name, output_name, preprocessed_data)

    return prediction


def preprocess(img):
    nparr = np.frombuffer(base64.b64decode(img), np.uint8)
    img_raw = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # convert to grayscale
    gray = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)

    # blur image to smooth outliers
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # apply thresholding to differentiate between foreground and background
    thresh = cv2.threshold(blur, 128, 255, cv2.THRESH_BINARY_INV)[1]

    # remove excess padding around number
    x, y, w, h = cv2.boundingRect(thresh)
    box = thresh[y:y + h, x:x + w]

    rows,cols = box.shape

    # resize image dimensions to fit within a 20x20 pixel box
    if rows > cols:
        factor = 20.0/rows
        rows = 20
        cols = int(round(cols*factor))
        box20 = cv2.resize(box, (cols,rows))
    else:
        factor = 20.0/cols
        cols = 20
        rows = int(round(rows*factor))
        box20 = cv2.resize(box, (cols, rows))

    # add padding to create a 28x28 pixel box
    colsPadding = (int(math.ceil((28-cols)/2.0)),int(math.floor((28-cols)/2.0)))
    rowsPadding = (int(math.ceil((28-rows)/2.0)),int(math.floor((28-rows)/2.0)))
    box28 = np.lib.pad(box20,(rowsPadding,colsPadding),'constant')

    # find center of mass of image and calculate the shift values for the x and y axis
    centerY,centerX = ndimage.center_of_mass(box28)
    rows,cols = box28.shape
    shiftX = np.round(cols/2.0-centerX).astype(int)
    shiftY = np.round(rows/2.0-centerY).astype(int)

    # shift image so that it conforms to the center of mass
    M = np.float32([[1,0,shiftX],[0,1,shiftY]])
    center = cv2.warpAffine(box28,M,(cols,rows))
    center.resize((1, 1, 28, 28))

    input_data = json.dumps({"data": center.tolist()})

    return input_data


def predict(session, input_name, output_name, input_data):
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
