from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum


class AdvertisementType(str, Enum):
    SELL = "sell"
    BUY = "buy"
    SERVICE = "service"


class AdvertisementBase(BaseModel):
    title: str
    description: str
    type: AdvertisementType


class AdvertisementCreate(AdvertisementBase):
    pass


class AdvertisementRead(AdvertisementBase):
    id: int
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True


class AdvertisementUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[AdvertisementType] = None
