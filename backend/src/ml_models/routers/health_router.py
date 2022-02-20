from fastapi import APIRouter

router = APIRouter()
prefix = "/v1"
tag = {
    "name": "General",
    "description": "Endpoints for monitoring and health checks",
}


@router.get("/health", summary="Health endpoint", tags=["General"])
async def health():
    return {"message": "Service is up and running"}
