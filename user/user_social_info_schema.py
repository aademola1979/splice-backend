from pydantic import BaseModel, Field
from datetime import date

class UserSocialInfoSchema(BaseModel):
    id: str
    user_id: str
    languages_spoken: str
    social_medial_profile: str
    religious_preference: str
    ethnic_group_preference: str
    allergies: str