from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

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
    name: str
    code: str
    zone_id: UUID
   
    
class StateResponseSchema(BaseModel):
    name: str
    code: str
    zone_id: UUID
    created_at: datetime
    updated_at: datetime