from pydantic import BaseModel, Field
from datetime import date

class LifestylePreferenceSchema(BaseModel):
    id: str
    user_id: str
    cooking_habits: str = 'rarely cook' | 'occasionally cook' | 'cook regularly'
    smoking_habits: str = 'non-smoker' | 'occasional smoker' | 'regular smoker'
    pet_ownership: str = 'no pets' | 'have pets' | 'prefer no pets' | 'open to pets'
    typical_sleep_schedule: str = 'early riser' | 'night owl' | 'flexible'
    cleanliness_level: int = 'very messy' | 'messy' | 'average' | 'clean' | 'very clean'
    guest_policy: str = 'no guests' | 'occasional guests' | 'frequent guests'
    noise_tolerance: str = 'very quiet' | 'moderate noise' | 'noisy environment' 
    work_from_home_frequency: str = '' | ''
    study_from_home_frequency: str
    work_shcedule: str
    age_range_of_preferred_co_renters: str
    utility_sharing_preferences: str
    preferred_gender_of_co_renters: str
    shared_space_expectations: str
    created_at: date
    updated_at: date
    deleted_at: date

