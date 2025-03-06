from sqlmodel import SQLModel, Field
from sqlalchemy import Column, ForeignKey
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime

class UserLifestylePreferencesModel(SQLModel, table=True):
    __tablename__ = "user_lifestyle_preferences"
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

    cooking_habits: str = Field(sa_column=Column('cooking_habits', pg.VARCHAR(225), nullable=True))
    smoking_habits: str = Field(sa_column=Column('smoking_habits', pg.VARCHAR(225), nullable=False))
    pet_ownership: str = Field(sa_column=Column('pet_ownership', pg.VARCHAR(225), nullable=False))
    typical_sleep_schedule: str = Field(sa_column=Column('typical_sleep_schedule', pg.VARCHAR(225), nullable=False))
    cleanliness: str = Field(sa_column=Column('cleanliness', pg.VARCHAR(225), nullable=False))
    guest_policy: str = Field(sa_column=Column('guest_policy', pg.VARCHAR(225), nullable=False))
    noise_tolerance: str = Field(sa_column=Column('noise_tolerance', pg.VARCHAR(225), nullable=False))
    work_from_home_frequency: str = Field(sa_column=Column('work_from_home_frequency', pg.VARCHAR(225), nullable=True))
    study_from_home_frequency: str = Field(sa_column=Column('study_from_home_frequency', pg.VARCHAR(225), nullable=True))
    work_schedule: str = Field(sa_column=Column('work_schedule', pg.VARCHAR(225), nullable=True))
    age_range_of_preferred_co_renters: str = Field(sa_column=Column('age_range_of_preferred_co_renters', pg.VARCHAR(225), nullable=False))
    utility_sharing_preferences: str = Field(sa_column=Column('utility_sharing_preference', pg.VARCHAR(225), nullable=False))
    preferred_gender_of_co_renters: str = Field(sa_column=Column('preferred_gender_of_co_renters', pg.VARCHAR(225), nullable=False))
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

    