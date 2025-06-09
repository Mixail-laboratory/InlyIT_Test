from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class TypeAdvert(str, Enum):
    vacancy = "vacancy"


class Advert(Base):
    __table_name__ = "adverts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="adverts")
    comments = relationship("Comment", back_populates="advert")