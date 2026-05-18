from fastapi import FastAPI

from app.db.init_db import init_db

app = FastAPI()

# Initialize database tables on startup
init_db()


@app.get("/")
def health():
    return {"status": "ok"}
