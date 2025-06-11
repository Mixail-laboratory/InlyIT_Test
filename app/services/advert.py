from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.advert import Advertisement
from models.user import User


async def create_advertisement(db: AsyncSession, ad_data, owner_id: int):
    db_ad = Advertisement(**ad_data.dict(), owner_id=owner_id)
    db.add(db_ad)
    await db.commit()
    await db.refresh(db_ad)
    return db_ad

async def get_advertisements(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(Advertisement)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()


async def get_advertisement(db: AsyncSession, ad_id: int):
    result = await db.execute(
        select(Advertisement)
        .where(Advertisement.id == ad_id)
    )
    return result.scalars().first()


async def delete_advertisement(db: AsyncSession, ad_id: int):
    ad = await get_advertisement(db, ad_id)
    if ad:
        await db.delete(ad)
        await db.commit()
