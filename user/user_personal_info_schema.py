from pydantic import BaseModel, Field
from datetime import date

class UserPersonalInfoSchema(BaseModel):
    id: str
    user_id: str
    email:str
    first_name: str
    last_name: str
    email: str
    mobile_phone: str
    password_hash: str
    is_verified: bool
    occupation: str
    created_at: date
    updated_at: date
    deleted_at: date
    
