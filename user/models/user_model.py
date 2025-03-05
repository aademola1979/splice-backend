from sqlmodel import SQLModel, Field
from sqlalchemy import Column
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime

class UserModel(SQLModel, table=True):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True}

    id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True, 
            index=True,
            nullable=False, 
            unique=True,
            default=uuid4
        ),  
    )
    first_name: str = Field(sa_column=Column('first_name', pg.VARCHAR(225), nullable=False))
    middle_name: str = Field(sa_column=Column('middle_name', pg.VARCHAR(225), nullable=True))
    last_name: str = Field(sa_column=Column('last_name', pg.VARCHAR(225), nullable=False))
    email: str = Field(sa_column=Column('email', pg.VARCHAR(225), nullable=False, unique=True))
    telephone: str = Field(sa_column=Column('telephone', pg.VARCHAR(225), nullable=False, unique=True))
    DOB: str 
    is_adult: bool = Field(sa_column=Column('is_adult', pg.BOOLEAN, default=False))
    is_verified: bool = Field(sa_column=Column('is_verified', pg.BOOLEAN, default=False))
    is_completed_registration: bool = Field(sa_column=Column('is_completed_registration', pg.BOOLEAN, default=False))
    created_at: datetime = Field(sa_column=Column('created_at', pg.TIMESTAMP, default=datetime.utcnow))
    updated_at: datetime = Field(sa_column=Column('updated_at', pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow))