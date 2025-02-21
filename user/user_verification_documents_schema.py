from pydantic import BaseModel
from datetime import date

class IDImageSchema(BaseModel):
    id: str
    document_id: str
    image_url: str

class UserVerificationDocumentsSchema(BaseModel):
    id: str
    user_id: str
    NIN: str
    id_image: IDImageSchema
    background_check_consent: bool