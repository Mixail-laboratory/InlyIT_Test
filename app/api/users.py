from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from schemas.advert import (
    AdvertisementCreate,
    AdvertisementRead,
    AdvertisementUpdate
)
from services.advert import (
    create_advertisement,
    get_advertisements,
    get_advertisement,
    delete_advertisement
)
from core.database import get_db
from core.security import get_current_user
from models.user import User

router = APIRouter()


@router.post("/ads", response_model=AdvertisementRead, status_code=status.HTTP_201_CREATED)
async def create_new_advertisement(
        ad_data: AdvertisementCreate,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return await create_advertisement(db, ad_data, current_user.id)


@router.get("/ads", response_model=List[AdvertisementRead])
async def read_all_advertisements(
        skip: int = 0,
        limit: int = 100,
        db: AsyncSession = Depends(get_db)
):
    return await get_advertisements(db, skip=skip, limit=limit)


@router.get("/ads/{ad_id}", response_model=AdvertisementRead)
async def read_advertisement_details(
        ad_id: int,
        db: AsyncSession = Depends(get_db)
):
    ad = await get_advertisement(db, ad_id)
    if not ad:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return ad


@router.delete("/ads/{ad_id}")
async def delete_user_advertisement(
        ad_id: int,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    ad = await get_advertisement(db, ad_id)
    if not ad:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    if ad.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    await delete_advertisement(db, ad_id)
    return {"message": "Advertisement deleted successfully"}

user_router = router
