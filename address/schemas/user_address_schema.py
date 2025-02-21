from pydantic import BaseModel
from datetime import date

class UserAddressSchema(BaseModel):
    id: str
    customer_id: str
    address_1 : str
    address_2: str
    city: str
    country_code: str
    _state: str
    lga: str
    created_at: date
    deleted_at: date
    updated_at: date
