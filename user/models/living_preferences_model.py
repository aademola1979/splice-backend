from sqlmodel import SQLModel, Field
from sqlalchemy import Column, ForeignKey
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime
from enum import Enum

class FurnishedState(str, Enum):
    furnished = 'furnished'
    semi_furnished = 'semi-furnished'
    unfurnished = 'unfurnished'

class UserLivingPreferencesModel(SQLModel, table=True):
    __tablename__ = "user_living_preferences"
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

    preferred_location_or_neighbourhood: str = Field(sa_column=Column('preferred_location_or_neighbourhood', pg.VARCHAR(225), nullable=True))
    required_furnished_state: str = Field(sa_column=Column('required_furnished_state', pg.ENUM(FurnishedState), nullable=False))
    preferred_number_of_co_renter: int = Field(sa_column=Column('preferred_number_of_co_renters', pg.NUMERIC, nullable=False))
    prefer_shared_bathroom: bool = Field(sa_column=Column('required_shared_bathroom', pg.BOOLEAN, nullable=False, default=False))
    require_parking_lots: bool = Field(sa_column=Column('require_parking_lots', pg.BOOLEAN, nullable=False, default=False))
    created_at: datetime = Field(sa_column=Column('created_at', pg.TIMESTAMP, default=datetime.utcnow))
    updated_at: datetime = Field(sa_column=Column('updated_at', pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow))

    # Foreign key column
    user_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("user.id"),
            nullable=False
        )
    )

    