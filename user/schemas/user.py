from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Union
from datetime import datetime


class UserSchema(BaseModel):
    id: UUID
    first_name: str = Field(..., min_length=3)
    middle_name: Union[str, None]
    last_name: str = Field(..., min_length=3)
    email: EmailStr = Field(..., min_length=3)
    telephone: str = Field(..., min_length=11)
    DOB: str
    is_adult: bool = False
    is_verified:bool = False
    is_completed_registration: bool = False
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
    first_name: str = Field(..., min_length=3)
    middle_name: Union[str, None] 
    last_name: str = Field(..., min_length=3)
    email: EmailStr = Field(..., min_length=3)
    telephone: str = Field(..., min_length=11)
    DOB: str
    is_adult: bool = False
    is_verified:bool = False
    is_completed_registration: bool = False
