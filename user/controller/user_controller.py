from sqlmodel.ext.asyncio.session import AsyncSession
from user.schemas.user import CreateUserShcema, UpdateUserSchema
from user.models.user_account_model import UserModel
from sqlmodel import select, desc
from database.database import async_session
from sqlmodel import text,UUID
from user.services import query_service
from lib.exceptions_classes import ResourcesNotFound, BaseAppException, UnauthorizedException, ValidationException
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserController:

    async def get_all_users(self, session:AsyncSession):
        statement = query_service.all_users_query
        try:
            result = await session.exec(statement=statement)
            if not result:
                raise ResourcesNotFound('Users not found')
            return result.all()
        except Exception as e:
            logger.exception('Error occurred while fetching users')
            raise BaseException('Internal error') from e
    
    

    async def get_user_by_id(self, user_id:str, session:AsyncSession):
        statement = query_service.get_user_by_id_query(user_id)
        try:
            result = await session.exec(statement=statement)
            if not result:
                raise ResourcesNotFound(f'Error occurred when trying to find user with user id {user_id}')
            user = result.first()
            return user
        except Exception as e:
            logger.exception("Error occurred fetching user")
            raise BaseAppException("Cannot fetch user") from e



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
        
    async def get_user_personal_info_by_id(self, user_id: UUID, session: AsyncSession):
        query = query_service.get_user_by_id_query(user_id)
        result = await session.exec(query)
        result = result.first()
        return result if result is not None else None
    
    async def get_user_personal_info_all(self, session: AsyncSession):
            query = query_service.all_detailed_address_query
            result = await session.exec(query)
            result = result.all()
            return result if result is not None else None
    

    async def get_user_personal_info_search(self, search_string:str, session: AsyncSession):
            query = query_service.detailed_address(search_string)
            result = await session.exec(query)
            result = result.all()
            return result if result is not None else None