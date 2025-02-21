from pydantic import BaseModel, Field
from datetime import date

class OnboardingState(BaseModel):
    id: str
    created_at: date
    updated_at: date
    current_step_id: str
    is_complete: bool
    user_id: str

