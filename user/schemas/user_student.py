from pydantic import BaseModel, Field
from datetime import date

class StudentSchema(BaseModel):
    id: str
    user_id: str
    institution_name: str
    course_of_study: str
    year_of_study: str
