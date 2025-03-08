from sqlmodel import SQLModel, Field
from sqlalchemy import Column, ForeignKey
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime
from enum import Enum

class DocumentType(str, Enum):
    voters_card = 'voter card'
    national_identification_card= 'national identificcaton card'
    divers_licence = 'driver licence'
    national_passport = 'national passport'
    international_passport = 'international passport'





class UserVrificatioDocumentModel(SQLModel, table=True):
    __tablename__ = "user_verification_document"
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

    document_type: str = Field(sa_column=Column('document_type', pg.ENUM(DocumentType), nullable=True, default=False))
    document_number: int = Field(sa_column=Column('document_number', pg.NUMERIC, nullable=False))
    document_url: str = Field(sa_column=Column('document_url', pg.BOOLEAN, nullable=False))
    user_passport_photgraph_url: str = Field(sa_column=Column('user_passport_photograph_url', pg.VARCHAR(225), nullable=False))
    user_document_is_verified: bool = Field(sa_column=Column('document_is_verified', pg.BOOLEAN, nullable=False, default=False))
    background_check_consent: bool = Field(sa_column=Column('background_check_consent', pg.BOOLEAN, nullable=True, default=False))
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

    