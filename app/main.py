from fastapi import FastAPI
from app.api.routes import router as users_router
from app.api.auth_routes import router as auth_router
from app.db.init_db import init_db

app = FastAPI()

init_db()  # creates database tables on startup

app.include_router(users_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "Python backend system is running"}
