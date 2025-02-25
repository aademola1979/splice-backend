from pydantic import BaseModel
from datetime import date

class LocalGovernmentAreaSchema(BaseModel):
    id: str
    name: str
    state_id: str
    created_at: date
    updated_at: date
    deleted_at: date
    
    
