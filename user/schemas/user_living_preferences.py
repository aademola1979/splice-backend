from pydantic import BaseModel, Field
from datetime import date
from typing import Literal

preferred_rent_payment_interval = Literal['monthly', 'annual']

class UserLivingPreferencesSchema(BaseModel):
    id: str
    user_id: str
    preferred_locations: str
    preferred_rent_payment_interval: preferred_rent_payment_interval
    furnnished: bool = False
    preferred_number_of_roommates: int = 0
    shared_bathroom: bool = False
    required_car_park: bool = False


