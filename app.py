from fastapi import FastAPI
from routes.ingest import router as ingest_router

app = FastAPI()

app.include_router(ingest_router)
