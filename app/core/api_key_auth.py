from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models.user import User


def get_current_user_from_api_key(
    x_api_key: str = Header(None),
    db: Session = Depends(get_db)
):
    if not x_api_key:
        raise HTTPException(
            status_code=401,
            detail="API key missing"
        )

    user = db.query(User).filter(User.api_key == x_api_key).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    return user
