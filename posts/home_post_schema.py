from pydantic import BaseModel, Field
from datetime import date
from post_schema import PostSchema



class HomePostSchema(BaseModel, PostSchema):
    home_type: str
    number_of_bedrooms: int
    number_of_kitchens: int
    number_of_bathrooms: int
