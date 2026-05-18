from fastapi import FastAPI

from app.api.routes import router as users_router
from app.api.auth_routes import router as auth_router
from app.api.billing_routes import router as billing_router
from app.api.webhooks import router as webhook_router

from app.db.init_db import init_db


app = FastAPI(
    title="Sextant Python Engine",
    description="SaaS Backend API with Auth + Billing + Stripe Integration",
    version="1.0.0"
)


# =========================
# DATABASE INITIALISATION
# =========================
@app.on_event("startup")
def startup():
    init_db()


# =========================
# ROUTES REGISTRATION
# =========================
app.include_router(users_router)
app.include_router(auth_router)

# 💰 SAAS MONETISATION LAYER
app.include_router(billing_router)
app.include_router(webhook_router)


# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def home():
    return {
        "status": "running",
        "service": "Sextant Python Engine"
    }
