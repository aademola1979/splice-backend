from pydantic import BaseModel, Field
from datetime import date

class UserFinancialInformation(BaseModel):
    user_id: str
    income_range: int
    annual_budget_range: int

