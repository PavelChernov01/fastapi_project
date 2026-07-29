from fastapi import FastAPI
from app.api.v1 import router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": f"Welcome to {settings.APP_NAME}"}
