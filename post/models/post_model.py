from sqlalchemy import Column, ForeignKey
from sqlmodel import SQLModel, Field
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime

class PostModel(SQLModel, table=True):
    __tablename__ = "post"
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


    description: str = Field(sa_column=Column('description', pg.VARCHAR(225), nullable=False))
    max_co_renter: int = Field(sa_column=Column('max_co_renter', pg.NUMERIC, nullable=False))
    rent: int = Field(sa_column=Column('rent', pg.BIGINT, nullable=False))
    caution_fee: int = Field(sa_column=Column('caution_fee', pg.BIGINT, nullable=True))
    agent_fee: int = Field(sa_column=Column('agent_fee', pg.BIGINT, nullable=True))
    total_fee: int = Field(sa_column=Column('total_fee', pg.BIGINT, nullable=False))
    created_at: datetime = Field(sa_column=Column('created_at', pg.TIMESTAMP, default=datetime.utcnow))
    updated_at: datetime = Field(sa_column=Column('updated_at', pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow))


    post_maker_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("user_account.id"),
            nullable=False
        )
    )

    post_type_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("post_types.id"),
            nullable=False
        )
    )

  

    

  
