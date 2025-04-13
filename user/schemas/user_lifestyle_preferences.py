from pydantic import BaseModel, Field
from datetime import date
from typing import Literal


cooking_habits = Literal['rarely cook', 'occasionally cook', 'cook regularly']
smoking_habits = Literal['non-smoker', 'occasional smoker', 'regular smoker']
pet_ownership_preferences = Literal['no pets', 'have pets', 'prefer no pets', 'open to pets']
typical_sleep_schedules = Literal['early riser', 'night owl', 'flexible']
cleanliness_levels = Literal['very messy', 'messy', 'average', 'clean', 'very clean']
guest_policies = Literal['no guests', 'occasional guests', 'frequent guests']
noise_tolrance_levels = Literal['very quiet', 'moderate noise', 'noisy environment']
work_from_home_frequencies = Literal['never', 'ocassionally', 'frequently', 'always']
study_from_home_frequencies = Literal['never', 'ocassionally', 'frequently', 'always']
work_schedules = Literal['remote', 'hybrid', 'office']
class LifestylePreferenceSchema(BaseModel):
    id: str
    user_id: str
    cooking_habit: cooking_habits
    smoking_habit: smoking_habits
    pet_ownership: pet_ownership_preferences
    typical_sleep_schedule: typical_sleep_schedules
    cleanliness_level: cleanliness_levels
    guest_policy: guest_policies
    noise_tolerance: noise_tolrance_levels 
    work_from_home_frequency: work_from_home_frequencies 
    study_from_home_frequency: study_from_home_frequencies
    work_shcedule: work_schedules
    age_range_of_preferred_co_renters: str
    utility_sharing_preferences: str
    preferred_gender_of_co_renters: str
    shared_space_expectations: str
    created_at: date
    updated_at: date
   

