from sqlalchemy.orm import Session
from src import models, schemas


def _find_all_users(db: Session) -> list[models.User]:
    """
    This helper function fetches all users from the database.
    Args:
        db (Session): SQLAlchemy session object.
    Returns:
        List[User]: List of User objects
    """
    query = db.query(models.User)
    return query.all()


def _find_user(db: Session, email: str = None, user_id: int = None) -> models.User:
    """
    This helper function fetches a user from the database based on email or user_id.
    Args:
        db (Session): SQLAlchemy session object.
        email (str): Email of the user.
        user_id (int): User ID.
    Returns:
        User: User object
    """
    query = db.query(models.User)
    if email:
        query = query.filter(models.User.email == email)
    elif user_id:
        query = query.filter(models.User.id == user_id)

    return query.first()


def _create_user(db: Session, user_details: schemas.UserCreateSchema) -> models.User:
    """
    This helper function creates a new user in the database.
    Args:
        db (Session): SQLAlchemy session object.
        user_details (User): User object.
    Returns:
        User: created User object
    """
    user_instance = models.User(
        email=user_details.email,
        first_name=user_details.first_name,
        last_name=user_details.last_name,
    )
    db.add(user_instance)
    db.commit()
    db.refresh(user_instance)
    return user_instance
