from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Union, Optional
from datetime import datetime, date


class UserSchema(BaseModel):
    id: UUID
    first_name: str
    middle_name: Union[str, None]
    last_name: str
    #hashed_password: Union[str, None]
    email: EmailStr
    telephone: str
    DOB: date
    created_at: datetime
    updated_at: datetime


class CreateUserShcema(BaseModel):
    first_name: str
    middle_name: str
    last_name: str 
    email: EmailStr 
    telephone: str 
    DOB: date
    


class UpdateUserSchema(BaseModel):
    first_name: str 
    middle_name: Union[str, None] = None
    last_name: str 
    email: EmailStr 
    telephone: str 
    DOB: date
    telephone: str
    


class UserResponseShcema(BaseModel):
    id:UUID
    first_name: str 
    middle_name: Union[str, None] 
    last_name: str
    email: EmailStr
    telephone: str 
    DOB: date
    

class UserAddressDetails(BaseModel):
    id:UUID
    first_name: str
    middle_name: Union[str, None] = None
    last_name: str
    email: EmailStr 
    street: str
    city: str
    lga_name: str
    state_name: str
    zone_name: str
