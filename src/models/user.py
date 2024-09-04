from src.settings.database import Base
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    blogs = relationship("Blog", back_populates="owner")
