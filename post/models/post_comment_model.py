from sqlalchemy import Column
from sqlmodel import SQLModel, Field, ForeignKey
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime

class PostCommentModel(SQLModel, table=True):
    __tablename__ = "post_comment"
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
    comment: str =Field(sa_column=Column('comment', pg.TEXT(), nullable=False))
    created_at: datetime = Field(sa_column=Column('created_at', pg.TIMESTAMP, default=datetime.utcnow))
    updated_at: datetime = Field(sa_column=Column('updated_at', pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow))

    post_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("post.id"),
            nullable=False
        )
    )

