import strawberry
from typing import List
from sqlalchemy.orm import Session
from src.models.user import User
from src.graphql.types.user.types import UserType
from src.graphql.types.blog.types import BlogType


@strawberry.type
class UserQuery:

    @strawberry.field
    def users(self, info) -> List[UserType]:
        db: Session = info.context["db"]
        users = db.query(User).all()
        return [
            UserType(
                id=user.id,
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                blogs=[
                    BlogType(
                        id=blog.id,
                        title=blog.title,
                        content=blog.content,
                        owner_id=blog.owner_id,
                    )
                    for blog in user.blogs
                ],
            )
            for user in users
        ]
