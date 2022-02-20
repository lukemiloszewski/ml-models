from fastapi import APIRouter

router = APIRouter()
prefix = "/v1"
tag = {
    "name": "General",
    "description": "Endpoints for service monitoring",
}


@router.get("/health", summary="Health Check", tags=["General"])
async def health():
    return {"message": "Service is up and running"}
