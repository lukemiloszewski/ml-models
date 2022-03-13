from fastapi import APIRouter

router = APIRouter()
prefix = ""
tag = {
    "name": "General",
    "description": "Endpoints for service monitoring",
}


@router.get("/", summary="Health Check", tags=["General"])
async def health():
    return {"message": "Service is up and running"}
