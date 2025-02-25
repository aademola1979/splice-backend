from pydantic import BaseModel, Field
from datetime import date

class UserFinancialInformation(BaseModel):
    user_id: str
    annual_rent_budget_range: int
    created_at: date
    updated_at: date
    deleted_at: date

