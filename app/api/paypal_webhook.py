from fastapi import APIRouter, Request, HTTPException
from app.db.session import SessionLocal
from app.models.user import User

router = APIRouter()
