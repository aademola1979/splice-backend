from pydantic import BaseModel, Field
from datetime import date

class LifestylePreferenceSchema(BaseModel):
    cooking_habits: str
    smoking_habits: str
    pet_ownership: str
    typical_sleep_schedule: str
    cleanliness_level: int
    guest_policy: str
    noise_tolerance: str
    work_from_home_frequency: str
    study_from_home_frequency: str
    work_shcedule: str
    age_range_of_preferred_co_renters: str
    utility_sharing_preferences: str
    preferred_gender_of_co_renters: str
    shared_space_expectations: str
    created_at: date
    updated_at: date
    deleted_at: date

