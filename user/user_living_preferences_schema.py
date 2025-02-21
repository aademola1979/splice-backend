from pydantic import BaseModel, Field
from datetime import date

class UserLivingPreferencesSchema(BaseModel):
    id: str
    user_id: str
    preferred_locations: str
    rent_payment_interval: str
    furnnished: bool
    preferred_number_of_roommate: int
    shared_bathroom: bool
    required_car_park: bool


