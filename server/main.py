from fastapi import FastAPI
from src.routes import (
    user_router,
    package_router
)

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(package_router, prefix="/packages", tags=["packages"])


@app.get("/")
async def root():
    return {"message": "Hello World"}