from pydantic import BaseModel
from typing import List

class IDImageSchema(BaseModel):
    id: str
    document_id: str
    image_url: str

class UserVerificationDocumentsSchema(BaseModel):
    id: str
    user_id: str
    national_identificcation_number: str
    id_image: List[IDImageSchema]
    background_check_consent: bool

