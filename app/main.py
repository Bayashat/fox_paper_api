from fastapi import FastAPI
from app.src.routers.views import researches, users, auth, comments, moderators

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(researches.router)
app.include_router(comments.router, prefix="/researches", tags=["comments"])
app.include_router(moderators.router, prefix="/moderators", tags=["moderators"])

