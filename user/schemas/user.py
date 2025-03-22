from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Union
from datetime import datetime


class UserSchema(BaseModel):
    id: UUID
    first_name: str
    middle_name: Union[str, None]
    last_name: str
    email: EmailStr
    telephone: str
    DOB: str
    created_at: datetime
    updated_at: datetime


class CreateUserShcema(BaseModel):
    first_name: str
    middle_name: str
    last_name: str 
    email: EmailStr 
    telephone: str 
    DOB: str
    is_adult: bool = False
    is_verified:bool = False
    is_completed_registration: bool = False


class UpdateUserSchema(BaseModel):
    first_name: str 
    middle_name: Union[str, None] = None
    last_name: str 
    email: EmailStr 
    telephone: str 
    DOB: str
    telephone: str
    is_adult: bool = False
    is_verified:bool = False
    is_completed_registration: bool = False


class UserResponseShcema(BaseModel):
    id:UUID
    first_name: str 
    middle_name: Union[str, None] 
    last_name: str
    email: EmailStr
    telephone: str 
    DOB: str
    

class UserAddressDetails(BaseModel):
    id:UUID
    first_name: str
    middle_name: Union[str, None] 
    last_name: str
    email: EmailStr 
    street: str
    city: str
    lga_name: str
    state_name: str
    zone_name: str
