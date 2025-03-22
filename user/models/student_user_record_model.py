from sqlmodel import SQLModel, Field, ForeignKey
from sqlalchemy import Column
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime
from enum import Enum


class StudentUserModel(SQLModel, table=True):
    __tablename__ = "student_user"
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

    
    institution_name: str = Field(sa_column=Column('institution_name', pg.VARCHAR(225), nullable=False))
    course_of_study: str = Field(sa_column=Column('course_of_study', pg.VARCHAR(225), nullable=True))
    year_of_study: str = Field(sa_column=Column('year_of_study', pg.VARCHAR(225), nullable=False))
    created_at: datetime = Field(sa_column=Column('created_at', pg.TIMESTAMP, default=datetime.utcnow))
    updated_at: datetime = Field(sa_column=Column('updated_at', pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow))

    user_account_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("user_account.id"),
            nullable=False
        )
    )
    
