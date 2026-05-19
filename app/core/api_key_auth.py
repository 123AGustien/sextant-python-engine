from fastapi import Header, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.api_key import APIKey
from app.services.api_key_service import verify_api_key


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def validate_api_key(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="API key missing")

    db = SessionLocal()

    try:
        keys = db.query(APIKey).filter(APIKey.is_active == True).all()

        for key in keys:
            if verify_api_key(x_api_key, key.key_hash):
                return True

        raise HTTPException(status_code=401, detail="Invalid API key")

    finally:
        db.close()
