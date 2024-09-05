import strawberry
from typing import List
from sqlalchemy.orm import Session
from src.models.user import User
from src.graphql.types.user.types import UserType
from src.graphql.types.blog.types import BlogType
from src.helpers import user


@strawberry.type
class UserQuery:

    @strawberry.field
    def users(self, info) -> List[UserType]:
        db: Session = info.context["db"]
        users = user._find_all_users(db=db)
        return [
            UserType(
                id=user_instance.id,
                first_name=user_instance.first_name,
                last_name=user_instance.last_name,
                email=user_instance.email,
                blogs=[
                    BlogType(
                        id=blog.id,
                        title=blog.title,
                        content=blog.content,
                        owner_id=blog.owner_id,
                    )
                    for blog in user_instance.blogs
                ],
            )
            for user_instance in users
        ]
