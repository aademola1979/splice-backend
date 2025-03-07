from sqlalchemy import Column, ForeignKey
from sqlmodel import SQLModel, Field
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime

class PostImageUrlModel(SQLModel, table=True):
    __tablename__ = "post_image_url"
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
    image_url: str =Field(sa_column=Column('image_url', pg.VARCHAR(225),nullable=False))
    created_at: datetime = Field(sa_column=Column('created_at', pg.TIMESTAMP, default=datetime.utcnow))
    updated_at: datetime = Field(sa_column=Column('updated_at', pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow))
    
    post_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("post.id"),
            nullable=False
        )
    )


