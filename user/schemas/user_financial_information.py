from pydantic import BaseModel, Field
from datetime import date
from typing import Literal
from uuid import UUID

annual_rent_budget_range = Literal[
    'below 100k', 
    'between 100k - 200k',
    'between 200k - 300k',
    'between 300k - 400k',
    'between 400k - 500k',
    'above 500k',
    ]

employment_status = Literal[
    'student',
    'professional',
    'business owner',
    'civil servant',
    'unemployed',
    'others'

    ]
class UserFinancialInformation(BaseModel):
    user_id: str
    employment_status: employment_status
    annual_rent_budget_range: annual_rent_budget_range
    created_at: date
    updated_at: date
    deleted_at: date
    user_account_id: UUID

