from fastapi import APIRouter, Depends
from app.middleware.auth_middleware import get_current_user

router = APIRouter()


@router.get("/me")
def read_me(current_user: str = Depends(get_current_user)):

    return {
        "user": current_user,
        "status": "authenticated",
        "message": "Identity verified"
    }
