import os
from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import AsyncGenerator

load_dotenv()

SQLALCHEMY_DATABSE_URL = f"{os.environ['SPLICE_DATABASE_URL']}"


async_engine = AsyncEngine(
    create_engine(
        url=SQLALCHEMY_DATABSE_URL, 
        echo=True,
        pool_size=10,
        max_overflow=20,
        )
    )

async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


async def init_db():
    async with async_engine.begin() as conn:
        from user.models.user_account_model import UserModel
        from address.models.zone_model import ZoneModel
        from address.models.local_government_model import LGAModel
        from user.models.user_lifestyle_prefrences_model import UserLifestylePreferencesModel
        from user.models.user_financial_information_model import UserFinancialInformationModel
        from user.models.user_address_model import UserAddressModel
        from post.models.post_type_model import PostTypesModel
        from post.models.post_model import PostModel
        from post.models.post_image_model import PostImageUrlModel
        from post.models.post_comment_model import PostCommentModel
        from user.models.additional_preferences_model import UserAdditionalPreferencesModel
        from user.models.living_preferences_model import UserLivingPreferencesModel
        from user.models.social_and_personal_preferences_model import UserSocialPersonalPreferencesModel
        from user.models.user_images_model import UserImageUrlModel
        from user.models.user_verification_documents import UserVrificatioDocumentModel
        from user.models.user_references_model import UserReferencesModel
        from user.models.student_user_record_model import StudentUserModel
        from user.models.user_attributes_model import UserAttributesModel
        
       
        await conn.run_sync(SQLModel.metadata.create_all)



async def get_session() -> AsyncGenerator[AsyncSession, None]:
    Session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with Session() as session:
        yield session

