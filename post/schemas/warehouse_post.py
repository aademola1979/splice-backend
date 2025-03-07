from pydantic import BaseModel, Field
from datetime import date
from post.schemas.post import PostSchema

class WarehouseSchema(BaseModel, PostSchema):
    pass