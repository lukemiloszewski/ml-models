import json

import cv2
from fastapi import APIRouter, Depends, File, UploadFile
from ml_models.services.mnist_service import predict_mnist
import numpy as np

from ml_models.context import Context
from ml_models.dependencies import get_context_dependency

router = APIRouter()
prefix = "/v1"
tag = {
    "name": "Models",
    "description": "Endpoints for machine learning models",
}


@router.post("/predict/mnist")
async def predict(image: UploadFile = File(...), context: Context = Depends(get_context_dependency)):
    content = await image.read()

    img_encoding = np.fromstring(content, np.uint8)
    img_raw = cv2.imdecode(img_encoding, cv2.IMREAD_COLOR)
    img = preprocess(img_raw)

    input_data = json.dumps({"data": img.tolist()})

    rv = predict_mnist(context, input_data)
    return rv


def preprocess(img):
    img_grayscaled = _convert_to_grayscale(img)
    img_processed = _resize(img_grayscaled)
    return img_processed


def _convert_to_grayscale(img):
    return np.dot(img[..., :3], [0.299, 0.587, 0.114])


def _resize(img):
    img_resized = cv2.resize(img, dsize=(28, 28), interpolation=cv2.INTER_AREA)
    img_resized.resize((1, 1, 28, 28))
    return img_resized
