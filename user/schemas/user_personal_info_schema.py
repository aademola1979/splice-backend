from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Union

class UserPersonalInfoSchema(BaseModel):
    id: str
    user_id: str
    email: EmailStr
    first_name: str
    middle_name: Union[str, None] = None
    last_name: str
    telephone: str
    hashed_password: Union[str, None] = None
    created_at: datetime
    updated_at: datetime

    

    


