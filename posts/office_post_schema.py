from pydantic import BaseModel, Field
from datetime import date
from post_schema import PostSchema

class OfficePostSchema(BaseModel, PostSchema):
    pass