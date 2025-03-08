from sqlmodel import SQLModel, Field
from sqlalchemy import Column, ForeignKey
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime
from enum import Enum


class PrefreferredGenderOfCorenters(str, Enum):
    male = 'male'
    female = 'female'
    no_preference = 'no preference'
class AgeRangeOfPreferredCoRenter(str, Enum):
    range_18_25 = '18-25'
    ranger_26_35 = '26-35'
    range_36_45 = '36-45'
    range_46_above = '46+'
class UtilitySharingPreferences(str, Enum):
    split_equally = 'split equally'
    based_on_usage = 'based on usage'
    included_in_rent = 'included in rent'


class UserAdditionalPreferencesModel(SQLModel, table=True):
    __tablename__ = "user_additional_preferences"
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

    
    age_range_of_preferred_co_renters: str = Field(sa_column=Column('age_range_of_preferred_co_renters', pg.ENUM(AgeRangeOfPreferredCoRenter), nullable=False))
    utility_sharing_preferences: str = Field(sa_column=Column('utility_sharing_preference', pg.ENUM(UtilitySharingPreferences), nullable=False))
    preferred_gender_of_co_renters: str = Field(sa_column=Column('preferred_gender_of_co_renters', pg.ENUM(PrefreferredGenderOfCorenters), nullable=False))
    shared_space_expectations: str = Field(sa_column=Column('shared_space_expectation', pg.TEXT(), nullable=True))
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

    