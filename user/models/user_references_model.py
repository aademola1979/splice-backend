from sqlmodel import SQLModel, Field
from sqlalchemy import Column, ForeignKey
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime
from enum import Enum


class ReferenceRelationship(str, Enum):
    parent = 'parent'
    sibling = 'sibling'
    friend = 'friend'
    colleague = 'colleague'
    no_preference = 'no preference'

class RefrenceCount(int, Enum):
    first_reference = 1
    second_reference = 2

class UtilitySharingPreferences(str, Enum):
    split_equally = 'split equally'
    based_on_usage = 'based on usage'
    included_in_rent = 'included in rent'


class UserReferencesModel(SQLModel, table=True):
    __tablename__ = "user_references"
    __table_args__ = {"extend_existing": True}

    id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True, 
            index=True,
            nullable=False, 
            unique=True,
            default=uuid4
        )  
    )

    first_name: str = Field(sa_column=Column('first_name', pg.VARCHAR(225), nullable=False))
    last_name: str = Field(sa_column=Column('last_name', pg.VARCHAR(225), nullable=False))
    email: str = Field(sa_column=Column('email', pg.VARCHAR(225), nullable=False))
    telephone: str = Field(sa_column=Column('telephone', pg.VARCHAR(225), nullable=False))
    reference_relationship: str = Field(sa_column=Column('reference_relationship', pg.ENUM(ReferenceRelationship), nullable=False))
    reference_count: int = Field(sa_column=Column('referrence_count', pg.ENUM(RefrenceCount), nullable=False))
    created_at: datetime = Field(sa_column=Column('created_at', pg.TIMESTAMP, default=datetime.utcnow))
    updated_at: datetime = Field(sa_column=Column('updated_at', pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow))

    # Foreign key column
    user_account_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("user_account.id"),
            nullable=False
        )
    )

    