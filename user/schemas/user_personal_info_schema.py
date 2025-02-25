from pydantic import BaseModel, validator, EmailStr
from datetime import date

class UserPersonalInfoSchema(BaseModel):
    id: str
    user_id: str
    email: EmailStr
    first_name: str
    last_name: str
    mobile_phone: str
    password_hash: str
    is_verified: bool = False
    created_at: date
    updated_at: date
    deleted_at: date
    user_work_status: str 

    


