from fastapi import FastAPI

from app.db.init_db import init_db
from app.api.auth_routes import router as auth_router
from app.api.protected_routes import router as protected_router
from app.api.tenant_routes import router as tenant_router

app = FastAPI()


# ---------------------------
# STARTUP (RAILWAY SAFE)
# ---------------------------
@app.on_event("startup")
def startup_event():
    init_db()


# ---------------------------
# ROUTES
# ---------------------------
app.include_router(auth_router)
app.include_router(protected_router)
app.include_router(tenant_router)


# ---------------------------
# HEALTH CHECK
# ---------------------------
@app.get("/")
def health():
    return {"status": "ok"}
