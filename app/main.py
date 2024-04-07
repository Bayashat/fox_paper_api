from fastapi import FastAPI
from .src.routers.views import auth, researches

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(researches.router, prefix="/researches", tags=["researches"])