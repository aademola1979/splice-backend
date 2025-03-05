import os
from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession

load_dotenv()

SQLALCHEMY_DATABSE_URL = f"{os.environ['SPLICE_DATABASE_URL']}"


async_engine = AsyncEngine(
    create_engine(
        url=SQLALCHEMY_DATABSE_URL, 
        echo=True
        )
    )
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=async_engine)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


async def init_db():
    async with async_engine.begin() as conn:
        from user.models.user_model import UserModel
        from address.models.zone_model import ZoneModel
        from address.models.local_government_model import LGAModel
        from address.models.address_model import AddressModel
        from user.models.use_lifestyle_prefrences_model import UserLifestylePreferencesModel
       
        await conn.run_sync(SQLModel.metadata.create_all)

from typing import AsyncGenerator

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    Session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with Session() as session:
        yield session