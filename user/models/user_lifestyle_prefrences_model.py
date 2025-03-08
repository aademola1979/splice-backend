from sqlmodel import SQLModel, Field
from sqlalchemy import Column, ForeignKey
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime
from enum import Enum

class CookingHabits(str, Enum):
    rarely_cook = 'rarely cook'
    occasionally_cook = 'occasionally cook'
    cook_regularly = 'cook regularly'

class SmokingHabits(str, Enum):
    non_smoking = 'non-smoking'
    occasional_smoker = 'occasional smoker'
    regular_smoker = 'regular smoker'

class PetOwnershipPrefrence(str, Enum):
    no_pets = 'no pets'
    have_pet = 'have pet'
    prefer_pets = 'prefer pets'
    prefer_no_pets = 'prefer no pets'
    open_to_pets = 'open to pets'

class TypicalSleepSchedule(str, Enum):
    early_riser = 'early rise'
    night_owl = 'night owl'
    flexible = 'flexible'

class Cleanliness(str, Enum):
    very_messy = 'very messy'
    average = 'average'
    very_clean = 'very clean'


class GuestPolicy(str, Enum):
    no_guests = 'no guests'
    occasional_guests = 'occasional guests'
    frequent_guests = 'frequent guests'


class NoiseTolerance(str, Enum):
    very_quiet = 'very_quiet'
    moderate_noise = 'moderate_noise'
    very_noisy = 'very noisy'

class WorkFromHomeFrequency(str, Enum):
    never = 'never'
    occasionally = 'occasionally'
    frequently = 'frequently'
    always = 'always'

class StudyFromHomeFrequency(str, Enum):
    never = 'never'
    occasionally = 'occasionally'
    frequently = 'frequently'
    always = 'always'

class WorkSchedule(str, Enum):
    remote = 'remote'
    hybrid = 'hybrid'
    office = 'office'



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

    cooking_habits: str = Field(sa_column=Column('cooking_habits', pg.ENUM(CookingHabits), nullable=True))
    smoking_habits: str = Field(sa_column=Column('smoking_habits', pg.ENUM(SmokingHabits), nullable=False))
    pet_ownership: str = Field(sa_column=Column('pet_ownership', pg.ENUM(PetOwnershipPrefrence), nullable=False))
    typical_sleep_schedule: str = Field(sa_column=Column('typical_sleep_schedule', pg.ENUM(TypicalSleepSchedule), nullable=False))
    cleanliness: str = Field(sa_column=Column('cleanliness', pg.ENUM(Cleanliness), nullable=False))
    guest_policy: str = Field(sa_column=Column('guest_policy', pg.ENUM(GuestPolicy), nullable=False))
    noise_tolerance: str = Field(sa_column=Column('noise_tolerance', pg.ENUM(NoiseTolerance), nullable=False))
    work_from_home_frequency: str = Field(sa_column=Column('work_from_home_frequency', pg.ENUM(WorkFromHomeFrequency), nullable=True))
    study_from_home_frequency: str = Field(sa_column=Column('study_from_home_frequency', pg.ENUM(StudyFromHomeFrequency), nullable=True))
    work_schedule: str = Field(sa_column=Column('work_schedule', pg.ENUM(WorkSchedule), nullable=True))
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

    