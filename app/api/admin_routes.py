from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models.user import User

router = APIRouter(prefix="/admin", tags=["Admin"])


# =========================
# GET ALL USERS
# =========================
@router.get("/users")
def get_users(db: Session = Depends(get_db)):

    users = db.query(User).all()

    return [
        {
            "id": u.id,
            "username": u.username,
            "plan": getattr(u, "plan", "free"),
            "api_key": u.api_key
        }
        for u in users
    ]
