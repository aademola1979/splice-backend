from fastapi import APIRouter, status, Depends
from user.models.user_model import UserModel
from user.schemas.user import UserSchema, UpdateUserSchema, UserResponseShcema, CreateUserShcema
from fastapi.exceptions import HTTPException
from database.database import get_session
from typing import List
from sqlalchemy.ext.asyncio.session import AsyncSession
from database.database import get_session
from user.controller.user_controller import UserController
from uuid import UUID

spec_router = APIRouter(prefix='/api/spec')

controller = UserController()

@spec_router.get("/")
async def my_user():
    users = await controller.get_specific_user()
    return users