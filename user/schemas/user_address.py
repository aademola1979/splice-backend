from pydantic import BaseModel 
from datetime import date

class UserAddressSchema(BaseModel):
    id: str
    name: str
    user_id: str
    postal_code: str
    local_government_id: str
    state_id: str
    zone_id: str
    created_at: date
    updated_at: date
    deleted_at: date
