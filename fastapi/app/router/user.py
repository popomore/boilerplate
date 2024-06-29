import logging

from fastapi import APIRouter, Depends

from app.model.user import UserModel
from app.service.user_service import UserService

router = APIRouter(prefix="/api/v1/user")
logger = logging.getLogger(__name__)


@router.get("/{user_id}")
async def get_user(
    user_id: int, user_service: UserService = Depends(UserService)
) -> UserModel:
    return await user_service.get_user(user_id)
