from pydantic import BaseModel, Field
from datetime import date

class ProfessionalOrBusinessOwnerSchema(BaseModel):
    id: str
    user_id: str
    industry_type: str
    work_schedule: str