from fastapi import APIRouter, Body, Depends

from ml_models.context import Context
from ml_models.dependencies import get_context_dependency
from ml_models.models.mnist_model import MnistRequest
from ml_models.services.mnist_service import get_mnist_prediction

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
    response = get_mnist_prediction(context=context, input_data=request.data)
    return {"result": response}
