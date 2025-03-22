from sqlmodel import SQLModel, Field
from sqlalchemy import Column, ForeignKey
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime
from enum import Enum

class ReligiousPreference(str, Enum):
    christianity = 'christianity'
    islam = 'islam'
    taditional = 'taditional'
    none = 'none'
    other = 'other'


class EnglishLanguageLevel(str, Enum):
    very_fluent = 'very fluent'
    fluent = 'fluent'
    poor = 'por'
    very_poor = 'very poor'





class UserSocialPersonalPreferencesModel(SQLModel, table=True):
    __tablename__ = "user_social_personal_preferences"
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

    english_language_level: str = Field(sa_column=Column('english_language_level', pg.ENUM(EnglishLanguageLevel), nullable=True, default=False))
    indigenous_language_spoken: str = Field(sa_column=Column('indigenous_language_spoken', pg.VARCHAR(225), nullable=True))
    can_speak_nigerian_pidgin_english: str = Field(sa_column=Column('can_speak_nigerian_pidgin_english', pg.BOOLEAN, nullable=True, default=False))
    hobbies: str = Field(sa_column=Column('hobbies', pg.VARCHAR(225), nullable=False))
    social_media_profile_link: str = Field(sa_column=Column('social_media_profile_link', pg.VARCHAR(225), nullable=False))
    religious_preference: bool = Field(sa_column=Column('religious_preference', pg.ENUM(ReligiousPreference), nullable=True))
    ethnic_group_proference: str = Field(sa_column=Column('ethnic_group_preference', pg.VARCHAR(225), nullable=False, default=True))
    created_at: datetime = Field(sa_column=Column('created_at', pg.TIMESTAMP, default=datetime.utcnow))
    updated_at: datetime = Field(sa_column=Column('updated_at', pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow))

    # Foreign key column
    user_account_id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            ForeignKey("user_account.id"),
            nullable=False
        )
    )

    