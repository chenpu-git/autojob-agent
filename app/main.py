from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.database import engine

app = FastAPI(title="AutoJob Agent", version="0.1.0")


@app.get("/health")
def health_check():
    try:
        with Session(engine) as session:
            session.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "database": str(e)}
