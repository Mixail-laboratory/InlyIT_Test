from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from core.database import Base
from schemas.advert import AdvertisementType
from datetime import datetime

class Advertisement(Base):
    __tablename__ = "advertisements"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    type = Column(Enum(AdvertisementType))
    owner_id = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime, default=datetime.utcnow)
    owner = relationship("User", back_populates="advertisements")
    comments = relationship("Comment", back_populates="advertisement")
