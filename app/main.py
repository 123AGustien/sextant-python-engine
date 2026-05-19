from fastapi import FastAPI
from app.db.init_db import init_db
from app.api import all_routers

app = FastAPI()


@app.on_event("startup")
def startup_event():
    init_db()


for router in all_routers:
    app.include_router(router)


@app.get("/")
def health():
    return {"status": "ok"}
