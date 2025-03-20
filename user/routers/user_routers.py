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


user_router = APIRouter(prefix='/api/user')

controller = UserController()


@user_router.get("/", response_model=List[UserSchema])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    users = await controller.get_all_user(session=session)
    return users 

@user_router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_new_user(user_data:CreateUserShcema, session: AsyncSession = Depends(get_session))->dict:
    new_user = await controller.create_user(user_data=user_data, session=session)
    return new_user

@user_router.get("/{user_id}", response_model=UserResponseShcema)
async def get_user_by_id(user_id:UUID, session: AsyncSession = Depends(get_session)):
    user = await controller.get_user_by_id(user_id=user_id, session = session)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@user_router.put("/{user_id}", response_model=UserResponseShcema)
async def update_user(user_id:UUID, update_data:UpdateUserSchema, session: AsyncSession = Depends(get_session)):
    user = await controller.update_user(user_id=user_id, update_data=update_data, session=session)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@user_router.delete("/{user_id}", response_model=None)
async def delete_user(user_id:UUID, session: AsyncSession = Depends(get_session)):
    user = await controller.delete_user(user_id=user_id, session=session)
    



