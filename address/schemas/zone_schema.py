from pydantic import BaseModel
from datetime import datetime 
from uuid import UUID


class ZoneSchema(BaseModel):
    id: UUID
    code: str 
    name: str
    created_at: datetime
    updated_at: datetime

class CreateZoneSchema(BaseModel):
    id: UUID
    code: str 
    name: str
    

class ZoneResponseSchema(BaseModel):
    id: UUID
    code: str 
    name: str
    created_at: datetime
    updated_at: datetime

class UpdateZoneSchema(BaseModel):
    id: UUID
    code: str 
    name: str

    