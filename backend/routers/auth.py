from fastapi import APIRouter
from app.utils.models import UserSchema
from app.utils.token_handler import sign_jwt


router = APIRouter()

@router.post("/api/login",tags=["auth"])
async def login_handler(user:UserSchema):
    token = sign_jwt(user.userid)
    return{"token": token}