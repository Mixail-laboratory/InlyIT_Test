from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __table_name__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    name = Column(String)
    admin = Column(Boolean, default=False)

    adverts = relationship("Advert", back_populates="owner")
    comments = relationship("Comment", back_populates="author")
