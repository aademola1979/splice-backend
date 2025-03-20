from sqlmodel.ext.asyncio.session import AsyncSession
from user.schemas.user import UserSchema, CreateUserShcema, UpdateUserSchema, UserResponseShcema
from user.models.user_model import UserModel
from sqlmodel import select, desc
from database.database import async_session
from sqlmodel import text

class UserController:

    async def get_all_user(self, session:AsyncSession):
        statement = select(UserModel).order_by(desc(UserModel.created_at))

        result = await session.exec(statement=statement)
        return result.all()

    async def get_user_by_id(self, user_id:str, session:AsyncSession):
        statement = select(UserModel).where(UserModel.id == user_id)

        result = await session.exec(statement=statement)

        user = result.first()

        return user if user is not None else None



    async def create_user(self, user_data:CreateUserShcema, session:AsyncSession):
        user_data_dict = user_data.model_dump()

        new_user = UserModel(**user_data_dict)

        session.add(new_user)

        await session.commit()

        return new_user

    async def update_user(self, user_id:str, update_data: UpdateUserSchema, session:AsyncSession):
        user_to_update = await self.get_user_by_id(user_id, session)

        if user_to_update is not None:
            update_data_dict = update_data.model_dump()
            for k, v in update_data_dict.items():
                setattr(user_to_update, k, v)
            
            await session.commit()
                
            return user_to_update
        
        else:
            return None


         

    
    async def delete_user(self, user_id:str, session:AsyncSession)->dict:
        user_to_delete = await self.get_user_by_id(user_id=user_id, session=session)

        if user_to_delete is not None:
            await session.delete(user_to_delete)
            await session.commit()
            return {"message":"User deleted successfully"}

        else:
            return None
        
    async def get_specific_user(self):
        query = select(text('id FROM user'))
        async with async_session() as session:
            result = await session.execute(query)
            user = result.all()
            return user