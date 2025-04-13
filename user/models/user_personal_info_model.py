from sqlmodel import SQLModel, Field
from sqlalchemy import Column, ForeignKey
import sqlalchemy.dialects.postgresql as pg
from uuid import uuid4, UUID
from datetime import datetime, date

class UserPersonalInfoModel(SQLModel, table=True):
    __tablename__ = "user_personal_info"
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
    telephone: str = Field(sa_column=Column('telephone', pg.VARCHAR(225), nullable=False, unique=True))
    DOB: date = Field(sa_column=Column('DOB', pg.DATE, nullable=False))
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
    created_at: datetime = Field(sa_column=Column('created_at', pg.TIMESTAMP, default=datetime.utcnow))
    updated_at: datetime = Field(sa_column=Column('updated_at', pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow))


