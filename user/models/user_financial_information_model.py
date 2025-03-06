from sqlmodel import SQLModel, Field
from sqlalchemy import Column, ForeignKey
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime

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
    
    income_range : str = Field(sa_column=Column('income_range', pg.VARCHAR(225), nullable=True))
    annual_rent_budget_range: str = Field(sa_column=Column('annual_rent_budget_range', pg.VARCHAR(225), nullable=False))
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

