from sqlmodel import SQLModel, Field
from sqlalchemy import Column
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime, date
from enum import Enum



class UserAttributesModel(SQLModel, table=True):
    __tablename__ = "user_attributes"
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


    is_fully_verified: bool = Field(sa_column=Column('is_fully_verified', pg.BOOLEAN, default=False))
    email_is_verified: bool = Field(sa_column=Column('email_is_verified', pg.BOOLEAN, nullable=True, default=False))
    is_subscribed: bool = Field(sa_column=Column('is_subscribed', pg.BOOLEAN, default=False))
    is_completed_registration: bool = Field(sa_column=Column('is_completed_registration', pg.BOOLEAN, default=False))
    remember_token: str = Field(sa_column=Column('string', pg.VARCHAR(225), nullable=True))
    user_national_identification_number_is_verified: bool = Field(sa_column=Column('user_national_identification_number_is_verified', pg.BOOLEAN, nullable=False, default=False))
    email_is_verified_at: datetime = Field(sa_column=Column('email_is_verified_at', pg.TIMESTAMP, nullable=True))
    created_at: datetime = Field(sa_column=Column('created_at', pg.TIMESTAMP, default=datetime.utcnow))
    updated_at: datetime = Field(sa_column=Column('updated_at', pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow))


