import base64
import json

import cv2
from fastapi import APIRouter, Body, Depends
import numpy as np

from ml_models.context import Context
from ml_models.dependencies import get_context_dependency
from ml_models.models.mnist_model import MnistRequest
from ml_models.services.mnist_service import predict_mnist, preprocess_mnist

router = APIRouter()
prefix = "/v1"
tag = {
    "name": "Models",
    "description": "Endpoints for machine learning models",
}


@router.post("/predict/mnist", summary="MNIST Prediction", tags=["Models"])
async def predict(
    request: MnistRequest = Body(...), context: Context = Depends(get_context_dependency)
):
    img_str = request.data
    img = preprocess_mnist(img_str)

    input_data = json.dumps({"data": img.tolist()})

    rv = predict_mnist(context, input_data)
    return rv
