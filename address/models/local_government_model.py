from sqlalchemy import Column, ForeignKey
from sqlmodel import SQLModel, Field
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime




class LGAModel(SQLModel, table=True):
    __tablename__ = "LGA"
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
    code: str = Field(sa_column=Column('code', pg.VARCHAR(225), nullable=False, unique=True))
    name: str = Field(sa_column=Column('name', pg.VARCHAR(225), nullable=False, unique=True))
    created_at: datetime = Field(sa_column=Column('created_at', pg.TIMESTAMP, default=datetime.utcnow))
    updated_at: datetime = Field(sa_column=Column('updated_at', pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow))
    
    # Foreign key column
    state_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("_state.id"),
            nullable=False
        )
    )