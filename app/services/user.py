from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from models.user import User
from schemas.user import UserCreate
from core.security import get_password_hash, verify_password


async def create_user(db: AsyncSession, user_data: UserCreate):
    hashed_password = get_password_hash(user_data.password)
    db_user = User(
        email=user_data.email,
        hashed_password=hashed_password,
        full_name=user_data.full_name,
        is_active=True
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_user_by_name(db: AsyncSession, name: str):
    result = await db.execute(
        select(User).where(User.full_name == name)
    )
    return result.scalars().first()


async def authenticate_user(db: AsyncSession, name: str, password: str):
    user = await get_user_by_name(db, name)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


async def make_admin(db: AsyncSession, user_id: int):
    await db.execute(
        update(User)
        .where(User.id == user_id)
        .values(is_admin=True)
    )
    await db.commit()
    return await get_user(db, user_id)
