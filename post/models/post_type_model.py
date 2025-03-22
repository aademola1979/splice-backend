from sqlalchemy import Column
from sqlmodel import SQLModel, Field
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime

class PostTypesModel(SQLModel, table=True):
    __tablename__ = "post_types"
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
    post_type: str = Field(sa_column=Column('post_type', pg.VARCHAR(225), nullable=False, unique=True))
    post_type_description: str = Field(sa_column=Column('description', pg.TEXT, nullable=True))
    code: str = Field(sa_column=Column('code', pg.VARCHAR(225), nullable=False, unique=True))
    created_at: datetime = Field(sa_column=Column('created_at', pg.TIMESTAMP, default=datetime.utcnow))
    updated_at: datetime = Field(sa_column=Column('updated_at', pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow))


