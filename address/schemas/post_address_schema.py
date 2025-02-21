from pydantic import BaseModel
from datetime import date

class PostAddressSchema(BaseModel):
    id: str
    post_id: str
    address : str
    city: str
    country_code: str
    _state: str
    lga: str
    created_at: date
    deleted_at: date
    updated_at: date
