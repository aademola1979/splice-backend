from pydantic import BaseModel
from datetime import date

class LGASchema(BaseModel):
    id: str
    name: str
    zone_id: str
    state_id: str
    created_at: date
    updated_at: date
    deleted_at: date
    
    
