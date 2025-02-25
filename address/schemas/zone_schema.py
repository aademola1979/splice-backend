from pydantic import BaseModel
from datetime import date
class RegionSchema(BaseModel):
    id: str
    code: str
    name: str
    created_at: date
    updated_at: date
    