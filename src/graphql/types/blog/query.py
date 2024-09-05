# types/blog/query.py
import strawberry
from typing import List
from sqlalchemy.orm import Session
from src.models.blog import Blog
from src.graphql.types.blog.types import BlogType
from src.helpers import blog


@strawberry.type
class BlogQuery:

    @strawberry.field
    def blogs(self, info) -> List[BlogType]:
        db: Session = info.context["db"]
        blogs = blog._find_all_blogs(db=db)
        return [
            BlogType(
                id=blog_instance.id,
                title=blog_instance.title,
                content=blog_instance.content,
                owner_id=blog_instance.owner_id,
            )
            for blog_instance in blogs
        ]
