from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.auth_service import (
    hash_password,
    verify_password
)

from app.core.security import create_access_token

router = APIRouter()

# temporary in-memory database
users_db = {}


class UserRegister(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


@router.post("/register")
def register(user: UserRegister):

    if user.username in users_db:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    hashed_pw = hash_password(user.password)

    users_db[user.username] = hashed_pw

    return {
        "message": "User registered successfully"
    }


@router.post("/login")
def login(user: UserLogin):

    if user.username not in users_db:
        raise HTTPException(
            status_code=400,
            detail="Invalid credentials"
        )

    stored_hash = users_db[user.username]

    if not verify_password(user.password, stored_hash):
        raise HTTPException(
            status_code=400,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": user.username}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
