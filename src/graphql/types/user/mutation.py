import strawberry
from sqlalchemy.orm import Session
from src.graphql.types.user.types import UserType
from fastapi import HTTPException, status
from src.helpers import user
from src import schemas


@strawberry.type
class UserMutation:

    @strawberry.mutation
    def create_user(
        self, info, first_name: str, last_name: str, email: str
    ) -> UserType:
        db: Session = info.context["db"]
        if user._find_user(db=db, email=email):
            raise HTTPException(
                detail=f"User with this email already exist.",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        user_info = schemas.UserCreateSchema(
            first_name=first_name, last_name=last_name, email=email
        )
        created_user = user._create_user(db=db, user_details=user_info)
        return UserType(
            id=created_user.id,
            first_name=created_user.first_name,
            last_name=created_user.last_name,
            email=created_user.email,
        )
