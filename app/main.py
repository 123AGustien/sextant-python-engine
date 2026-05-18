from fastapi import FastAPI

from app.api.routes import router as users_router
from app.api.auth_routes import router as auth_router
from app.api.billing_routes import router as billing_router
from app.api.webhooks import router as webhook_router

from app.db.init_db import init_db

app = FastAPI()


# =========================
# STARTUP (DB INIT)
# =========================
@app.on_event("startup")
def startup():
    init_db()


# =========================
# ROUTES
# =========================
app.include_router(users_router)
app.include_router(auth_router)

# 💰 STEP 13: MONETISATION ROUTES
app.include_router(billing_router)
app.include_router(webhook_router)


# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def home():
    return {"message": "Python backend system is running"}
