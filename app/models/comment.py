from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from core.database import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(500), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    author_id = Column(Integer, ForeignKey("users.id"))
    advertisement_id = Column(Integer, ForeignKey("advertisements.id"))

    author = relationship("User", back_populates="comments")
    advertisement = relationship("Advertisement", back_populates="comments")
