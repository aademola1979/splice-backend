from sqlalchemy import Column, ForeignKey
from sqlmodel import SQLModel, Field
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime


class UserAddressModel(SQLModel, table=True):
    __tablename__ = "user_address"
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
    street: str = Field(sa_column=Column('street', pg.VARCHAR(225), nullable=False))
    city: str = Field(sa_column=Column('city', pg.VARCHAR(225), nullable=False))
   
     # Foreign key column
    lga_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("local_government_area.id"),
            nullable=False
        )
    )

    # Foreign key column
    state_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("_state.id"),
            nullable=False
        )
    )
      # Foreign key column
    user_account_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("user_account.id"),
            nullable=False
        )
    )
    created_at: datetime = Field(sa_column=Column('created_at', pg.TIMESTAMP, default=datetime.utcnow))
    updated_at: datetime = Field(sa_column=Column('updated_at', pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow))
    

