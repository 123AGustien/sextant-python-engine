from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models.user import User

from app.services.auth_service import (
    hash_password,
    verify_password
)

from app.core.security import create_access_token
from app.services.api_key_service import generate_api_key

router = APIRouter()


# =========================
# REQUEST MODELS
# =========================

class UserRegister(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


# =========================
# REGISTER USER (SAAS READY)
# =========================

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    # check if user exists
    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    # hash password
    hashed_pw = hash_password(user.password)

    # generate API key (monetisation layer)
    api_key = generate_api_key()

    # create user
    new_user = User(
        username=user.username,
        password=hashed_pw,
        api_key=api_key
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id,
        "api_key": new_user.api_key
    }


# =========================
# LOGIN USER (SAAS READY)
# =========================

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Invalid credentials"
        )

    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=400,
            detail="Invalid credentials"
        )

    # JWT token for session auth
    token = create_access_token(
        {"sub": db_user.username}
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "api_key": db_user.api_key
    }
