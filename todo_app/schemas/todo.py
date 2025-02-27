from pydantic import BaseModel

class TodoRequest(BaseModel):
    name: str
    completed: bool


class TodoResponse(BaseModel):
    name: str
    completed: bool
    id: int

    class Config:
        from_attributes: True