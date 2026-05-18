from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models.user import User
from app.core.rate_limit import FREE_LIMIT, PRO_LIMIT


def check_rate_limit(username: str, db: Session):

    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    limit = PRO_LIMIT if getattr(user, "plan", "free") == "pro" else FREE_LIMIT

    if user.request_count >= limit:
        raise HTTPException(
            status_code=429,
            detail="API limit reached. Upgrade plan."
        )

    user.request_count += 1
    db.commit()

    return user
