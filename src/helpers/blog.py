from sqlalchemy.orm import Session
from src import models, schemas


def _find_all_blogs(db: Session) -> list[models.Blog]:
    """
    This helper function fetches all blogs from the database.
    Args:
        db (Session): SQLAlchemy session object.
    Returns:
        List[Blog]: List of Blog objects
    """
    query = db.query(models.Blog)
    return query.all()


def _create_blog(db: Session, blog_details: schemas.BlogCreateSchema) -> models.Blog:
    """
    This helper function creates a new blog in the database.
    Args:
        db (Session): SQLAlchemy session object.
        blog_details (Blog): Blog object.
    """
    blog_instance = models.Blog(
        title=blog_details.title,
        content=blog_details.content,
        owner_id=blog_details.owner_id,
    )
    db.add(blog_instance)
    db.commit()
    db.refresh(blog_instance)
    return blog_instance
