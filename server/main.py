from fastapi import FastAPI
from src.routes import (
    user_router,
)

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])


@app.get("/")
async def root():
    return {"message": "Hello World"}