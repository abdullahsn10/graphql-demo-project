# types/blog/mutation.py
import strawberry
from sqlalchemy.orm import Session
from src.models.blog import Blog
from src.graphql.types.blog.types import BlogType
from src.models.user import User
from fastapi import HTTPException, status


@strawberry.type
class BlogMutation:

    @strawberry.mutation
    def create_blog(self, info, title: str, content: str, owner_id: int) -> BlogType:
        db: Session = info.context["db"]
        # Check if the owner (user) exists
        owner = db.query(User).filter(User.id == owner_id).first()
        if not owner:
            raise HTTPException(
                detail=f"User with id {owner_id} does not exist.",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        blog = Blog(title=title, content=content, owner_id=owner_id)
        db.add(blog)
        db.commit()
        db.refresh(blog)
        return BlogType(
            id=blog.id, title=blog.title, content=blog.content, owner_id=blog.owner_id
        )
