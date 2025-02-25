from pydantic import BaseModel, Field
from datetime import date
from posts.schemas.post import PostSchema

class OfficePostSchema(BaseModel, PostSchema):
    pass