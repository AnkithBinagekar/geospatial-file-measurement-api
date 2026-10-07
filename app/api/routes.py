from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["System"])
def health_check():
    """
    Verifies that the API server is up and routing correctly.
    """
    return {
        "status": "ok",
        "message": "Geospatial API is running."
    }