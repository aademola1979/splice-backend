from pydantic import BaseModel
from datetime import date

class CitySchema(BaseModel):
    id: str
    name: str
    postal_code: str
    is_capital: bool
    lga_id: str
    created_at: date
    updated_at: date
    deleted_at: date