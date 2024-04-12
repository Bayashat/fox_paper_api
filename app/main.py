from fastapi import FastAPI
from app.src.routers.views import researches, users, auth, comments

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(researches.router, prefix="/researches", tags=["researches"])
app.include_router(comments.router, prefix="/researches", tags=["comments"])

