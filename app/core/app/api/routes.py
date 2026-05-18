from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.core.rate_limiter import check_rate_limit

router = APIRouter()


@router.get("/data")
def get_data(username: str, db: Session = Depends(get_db)):

    user = check_rate_limit(username, db)

    return {
        "message": "Here is your protected data",
        "user": user.username,
        "requests_used": user.request_count
    }
