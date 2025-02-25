from pydantic import BaseModel
from datetime import date

class StateSchema(BaseModel):
    id: str
    name: str
    code: int
    zone_id: str
    created_at: date
    updated_at: date
    deleted_at: date