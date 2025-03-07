from pydantic import BaseModel, Field
from datetime import date


class PostImage(BaseModel):
    image_id: str
    image_url: str
    created_at: str
    updated_at: str



class PostSchema(BaseModel):
    post_id: str
    user_id: str
    post_type_id: str
    comment_id: str
    post_description: str
    post_images: PostImage
    max_co_renter: int
    rent_fee: int
    caution_fee: int
    agent_fee: int
    total_fee: int
    total_fee: int
    post_address_id: str
   

    