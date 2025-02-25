from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional

class OtherLanguages(BaseModel):
    name: str

class SocialMediaProfile(BaseModel):
    name: str
    url: str

class Religion(BaseModel):
    name: str

class EthnicGroup(BaseModel):
    name: str

class Allergy(BaseModel):
    name: str

class UserSocialInfoSchema(BaseModel):
    id: str
    user_id: str
    speaks_english: bool = True
    speaks_nigerian_pidgin: bool
    other_languages_spoken: Optional[List[OtherLanguages]]
    social_medial_profile: Optional[List[SocialMediaProfile]]
    religious_preference: Optional[List[Religion]]
    ethnic_group_preference: Optional[List[EthnicGroup]]
    allergies: Optional[List[Allergy]]