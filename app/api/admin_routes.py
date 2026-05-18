from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models.user import User

router = APIRouter(prefix="/admin", tags=["Admin"])


# =========================
# SIMPLE ADMIN SECURITY
# =========================
ADMIN_SECRET = "change_this_admin_key"


def verify_admin(x_admin_key: str = Header(None)):

    if x_admin_key != ADMIN_SECRET:
        raise HTTPException(status_code=403, detail="Forbidden")


# =========================
# GET ALL USERS
# =========================
@router.get("/users")
def get_users(
    db: Session = Depends(get_db),
    _: None = Depends(verify_admin)
):

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


# =========================
# SaaS STATS
# =========================
@router.get("/stats")
def get_stats(
    db: Session = Depends(get_db),
    _: None = Depends(verify_admin)
):

    total_users = db.query(User).count()

    # SAFE handling (prevents crash if column missing or NULL)
    pro_users = db.query(User).filter(
        (User.plan == "pro")
    ).count()

    return {
        "total_users": total_users,
        "pro_users": pro_users,
        "estimated_monthly_revenue": pro_users * 10
    }
