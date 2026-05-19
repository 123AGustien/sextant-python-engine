from fastapi import Request, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.services.api_key_service import get_api_key
from app.core.api_keys import verify_api_key


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
# API KEY MIDDLEWARE LOGIC
# ---------------------------
async def api_key_guard(request: Request, call_next):
    """
    Protect routes using API key authentication.
    """

    # Allow public routes
    if request.url.path in ["/", "/docs", "/openapi.json"]:
        return await call_next(request)

    api_key = request.headers.get("x-api-key")

    if not api_key:
        raise HTTPException(status_code=401, detail="API key missing")

    db = SessionLocal()

    try:
        record = get_api_key(db, api_key)

        if not record:
            raise HTTPException(status_code=401, detail="Invalid API key")

        # verify hash
        if not verify_api_key(api_key, record.key_hash):
            raise HTTPException(status_code=401, detail="API key verification failed")

        # attach tenant context
        request.state.user_id = record.user_id
        request.state.tenant_id = record.tenant_id

        response = await call_next(request)
        return response

    finally:
        db.close()
