# types/blog/query.py
import strawberry
from typing import List
from sqlalchemy.orm import Session
from src.models.blog import Blog
from src.graphql.types.blog.types import BlogType


@strawberry.type
class BlogQuery:

    @strawberry.field
    def blogs(self, info) -> List[BlogType]:
        db: Session = info.context["db"]
        blogs = db.query(Blog).all()
        return [
            BlogType(
                id=blog.id,
                title=blog.title,
                content=blog.content,
                owner_id=blog.owner_id,
            )
            for blog in blogs
        ]
