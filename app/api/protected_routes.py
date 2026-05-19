from fastapi import APIRouter, Depends
from app.core.guards import protected_route

router = APIRouter()


@router.get("/secure-data")
def secure_data(auth=Depends(protected_route)):

    return {
        "message": "You are inside the secured system",
        "user": auth["user"],
        "access": auth["api_access"]
    }
