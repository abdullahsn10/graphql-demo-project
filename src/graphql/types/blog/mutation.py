import strawberry
from sqlalchemy.orm import Session
from src.graphql.types.blog.types import BlogType
from fastapi import HTTPException, status
from src.helpers import blog, user
from src import schemas


@strawberry.type
class BlogMutation:

    @strawberry.mutation
    def create_blog(self, info, title: str, content: str, owner_id: int) -> BlogType:
        db: Session = info.context["db"]
        # Check if the owner (user) exists
        owner = user._find_user(db=db, user_id=owner_id)
        if not owner:
            raise HTTPException(
                detail=f"User with id {owner_id} does not exist.",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        blog_details = schemas.BlogCreateSchema(
            title=title, content=content, owner_id=owner.id
        )
        created_blog = blog._create_blog(db=db, blog_details=blog_details)
        return BlogType(
            id=created_blog.id,
            title=created_blog.title,
            content=created_blog.content,
            owner_id=created_blog.owner_id,
        )
