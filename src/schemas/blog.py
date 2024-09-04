from pydantic import BaseModel


class BlogSchema(BaseModel):
    """
    Blog Schema
    """

    id: int
    title: str
    content: str
    owner_id: int

    class Config:
        orm_mode = True
