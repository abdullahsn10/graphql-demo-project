import strawberry
from typing import List, Optional
from dataclasses import field
from src.graphql.types.blog.types import BlogType


@strawberry.type
class UserType:
    id: int
    first_name: str
    last_name: str
    email: str
    blogs: Optional[List[BlogType]] = field(default_factory=list)
