from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    username = Column(String)
    is_admin = Column(Boolean, default=False)

    adverts = relationship("Advert", back_populates="owner")
    comments = relationship("Comment", back_populates="author")
