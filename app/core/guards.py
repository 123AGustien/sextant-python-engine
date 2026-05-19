from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.api_key import APIKey
from app.services.api_key_service import verify_api_key
from app.core.security import get_current_user


# ---------------------------
# DB SESSION
# ---------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------
# API KEY VALIDATION
# ---------------------------
def validate_api_key(x_api_key: str = Header(None), db: Session = Depends(get_db)):

    if not x_api_key:
        raise HTTPException(status_code=401, detail="API key missing")

    keys = db.query(APIKey).filter(APIKey.is_active == True).all()

    for key in keys:
        if verify_api_key(x_api_key, key.key_hash):
            return True

    raise HTTPException(status_code=401, detail="Invalid API key")


# ---------------------------
# COMBINED SECURITY GUARD
# ---------------------------
def protected_route(
    user=Depends(get_current_user),
    api_key_valid=Depends(validate_api_key)
):
    """
    Pass-through dependency:
    Only allows access if BOTH are valid
    """
    return {
        "user": user,
        "api_access": True
    }
