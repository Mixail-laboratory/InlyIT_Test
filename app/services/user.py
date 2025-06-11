from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from models.user import User
from schemas.user import UserCreate
from core.security import (get_password_hash, verify_password, get_user_by_name, get_user_by_uid)


async def create_user(db: AsyncSession, user_data: UserCreate):
    hashed_password = get_password_hash(user_data.password)
    db_user = User(
        email=user_data.email,
        hashed_password=hashed_password,
        full_name=user_data.full_name,
        is_active=True,
        is_admin=user_data.is_admin
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def authenticate_user(db: AsyncSession, name: str, password: str):
    user = await get_user_by_name(db, name)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


async def update_user_admin(
        db: AsyncSession,
        user_id: int,
        update_data: dict
) -> User:
    db_user = await get_user_by_uid(db, user_id)
    if not db_user:
        return None

    for field, value in update_data.items():
        setattr(db_user, field, value)

    await db.commit()
    await db.refresh(db_user)
    return db_user
