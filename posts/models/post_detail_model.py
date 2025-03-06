from sqlalchemy import Column, ForeignKey
from sqlmodel import SQLModel, Field
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime

class PostModel(SQLModel):
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
    rent_fee: int = Field(sa_column=Column('rent_fee', pg.BIGINT, nullable=False))
    caution_fee: int = Field(sa_column=Column('caution fee', pg.BIGINT, nullable=False))
    agent_fee: int = Field(sa_column=Column('agent', pg.BIGINT, nullable=False))
    total_fee: int = Field(sa_column=Column('smoking_habits', pg.BIGINT, nullable=False))
    total_fee: int = Field(sa_column=Column('smoking_habits', pg.BIGINT, nullable=False))
    created_at: datetime = Field(sa_column=Column('created_at', pg.TIMESTAMP, default=datetime.utcnow))
    updated_at: datetime = Field(sa_column=Column('updated_at', pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow))


    user_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("user.id"),
            nullable=False
        )
    )

    post_type_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("post_type.id"),
            nullable=False
        )
    )

    post_address_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("post_address.id"),
            nullable=False
        )
    )

    post_image_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("post_image.id"),
            nullable=False
        )
    )

    post_comment_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("post_comment.id"),
            nullable=False
        )
    )
