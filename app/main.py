from fastapi import FastAPI

from app.config import settings
from app.routes.qr_code import router as qr_code_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)


app.include_router(qr_code_router)