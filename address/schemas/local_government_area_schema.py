from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class LocalGovernmentAreaSchema(BaseModel):
    id: UUID
    name: str
    code: str
    state_id: UUID
    created_at: datetime
    updated_at: datetime

    
class LocalGovernmentAreaWithStateSchema(BaseModel):
    local_government_name: str
    local_government_code: str
    local_government_id: UUID
    state_name: str
    state_code: str
    state_id: UUID
    zone_name: str
    zone_code: str
    zone_id: UUID

class UpdateLGASchema(BaseModel):
    name: str
    code: str
    state_id: UUID

class CreateLocalGovernmentAreaSchema(BaseModel):
    name: str
    code: str
    state_id: UUID