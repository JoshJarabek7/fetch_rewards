from fastapi import FastAPI
from app.api.endpoints.receipts import router as receipts_router

app = FastAPI()
app.include_router(receipts_router)