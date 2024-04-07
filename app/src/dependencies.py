# async def verify_jwt(credentials: HTTPAuthorizationCredentials) -> bool:
#     token = str(credentials.credentials)
#     try:
#         response = await AsyncRequestClient.make_request(
#             method="GET",
#             url="https://api.technodom.kz/sso/api/v1/profile",
#             headers={"Authorization": f"Bearer {token}"},
#         )
#         response.raise_for_status()
#         return True
#     except httpx.HTTPStatusError as e:
#         raise HTTPException(
#             detail=f"HTTP error occurred: {e}", status_code=e.response.status_code
#         )
#     except httpx.RequestError as e:
#         raise HTTPException(detail=f"Request error occurred: {e}", status_code=500)




# class JWTBearer(HTTPBearer):
#     async def __call__(self, request: Request):
#         credentials: HTTPAuthorizationCredentials | None = await super(
#             JWTBearer, self
#         ).__call__(request)
#         if credentials and await verify_jwt(credentials):
#             return credentials.credentials
#         else:
#             return None

from jose import jwt
from fastapi.security import OAuth2PasswordBearer as OA
from app.src.database import SessionLocal

# JWT part
def create_jwt(user_id: int) -> str:
    body = {"user_id": user_id}
    token = jwt.encode(body, "fox_paper", algorithm="HS256")
    return token
    
def decode_jwt(token: str) -> int:
    data = jwt.decode(token, "fox_paper", algorithms="HS256")
    return data["user_id"]

# Database part
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()
        
oauth2_scheme = OA(tokenUrl="/auth/users/login")