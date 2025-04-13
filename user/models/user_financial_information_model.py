from sqlmodel import SQLModel, Field
from enum import Enum
from sqlalchemy import Column, ForeignKey
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime


class AnnualRentBudgetRange(str, Enum):
    below_100k = 'below 100k'
    between_100k_200k = 'between 100k - 200k'
    between_200k_300k = 'between 200k - 300k'
    between_300k_400k = 'between 300k - 400k'
    between_400k_500k = 'between 400k - 500k'
    above_100k = 'above 500k'

class EmploymentStatus(str, Enum):
    student = 'student'
    professional = 'professional'
    business_owner = 'business owner'
    civil_servant = 'civil servant'
    unemployed = 'unemployed'
    other = 'others'


class UserFinancialInformationModel(SQLModel, table=True):
    __tablename__ = "user_financial_information"
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
    
    employment_status: str = Field(sa_column=Column('employment_status', pg.ENUM(EmploymentStatus), nullable=False))
    annual_rent_budget_range: str = Field(sa_column=Column('annual_rent_budget_range', pg.ENUM(AnnualRentBudgetRange), nullable=False))
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

