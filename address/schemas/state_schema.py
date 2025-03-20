from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from address.schemas.zone_schema import ZoneSchema

class StateSchema(BaseModel):
    id: UUID
    name: str
    code: str
    zone_id: UUID
    created_at: datetime
    updated_at: datetime


class CreateStateSchema(BaseModel):
    name: str
    code: str
    zone_id: UUID

class UpdateStateSchema(BaseModel):
    id: UUID
    name: str
    code: str
    zone_id: UUID
   
    
class StateResponseSchema(BaseModel):
    id: UUID
    name: str
    code: str
    zone_id: UUID
    created_at: datetime
    updated_at: datetime


class StateResponseWithZoneSchema(BaseModel):
    id: UUID
    name: str
    code: str
    zone_name: str
    zone_name: str
    created_at: datetime
    updated_at: datetime

class StateWithZoneSchema(BaseModel):
    local_government_name: str
    state_name: str
    zone_name: str
    local_government_id: UUID

