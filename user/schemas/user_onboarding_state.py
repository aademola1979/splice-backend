from pydantic import BaseModel
from datetime import date

class OnboardingState(BaseModel):
    id: str
    user_id: str
    created_at: date
    updated_at: date
    current_step_id: str
    is_complete: bool = False


