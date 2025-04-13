from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Union, Optional
from datetime import datetime, date


class UserSchema(BaseModel):
    id: UUID
    first_name: str
    middle_name: Union[str, None] = None
    last_name: str
    hashed_password: Union[str, None] = None
    email: EmailStr
    created_at: datetime
    updated_at: datetime


class CreateUserShcema(BaseModel):
    first_name: str
    middle_name: Union[str, None] = None
    last_name: str 
    hashed_password: Union[str, None] =None
    email: EmailStr 
    
    


class UpdateUserSchema(BaseModel):
    first_name: str 
    middle_name: Union[str, None] = None
    last_name: str 
    hashed_password: Union[str, None] = None
    email: EmailStr
    updated_at: datetime
    
    


class UserResponseShcema(BaseModel):
    id:UUID
    first_name: str 
    middle_name: Union[str, None] 
    last_name: str
    email: EmailStr
   
    

class UserPersonalInfo(BaseModel):
    id:UUID
    first_name: str
    middle_name: Union[str, None] = None
    last_name: str
    email: EmailStr
    DOB: date
    telephone: str 
    street: str
    city: str
    lga_name: str
    state_name: str
    zone_name: str
