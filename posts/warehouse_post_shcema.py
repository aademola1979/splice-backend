from pydantic import BaseModel, Field
from datetime import date
from post_schema import PostSchema

class WarehouseSchema(BaseModel, PostSchema):
    pass