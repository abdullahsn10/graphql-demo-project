from pydantic import BaseModel
from typing import List, Optional
from src.schemas.blog import BlogSchema


class UserSchema(BaseModel):
    """
    User Schema
    """

    id: int
    email: str
    first_name: str
    last_name: str
    blogs: Optional[List[BlogSchema]]

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    """
    User Create Schema
    """

    email: str
    first_name: str
    last_name: str
