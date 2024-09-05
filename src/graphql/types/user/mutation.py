import strawberry
from sqlalchemy.orm import Session
from src.models.user import User
from src.graphql.types.user.types import UserType
from fastapi import HTTPException, status


@strawberry.type
class UserMutation:

    @strawberry.mutation
    def create_user(
        self, info, first_name: str, last_name: str, email: str
    ) -> UserType:
        db: Session = info.context["db"]
        # Check if the email already exists
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            raise HTTPException(
                detail=f"User with this email already exist.",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        user = User(first_name=first_name, last_name=last_name, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return UserType(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
        )
