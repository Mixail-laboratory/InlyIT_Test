from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.comment import Comment
from schemas.comment import CommentCreate


async def create_comment(db: AsyncSession, comment_data: CommentCreate, author_id: int):
    db_comment = Comment(**comment_data.dict(), author_id=author_id)
    db.add(db_comment)
    await db.commit()
    await db.refresh(db_comment)
    return db_comment


async def get_comments(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(Comment)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()


async def get_comment(db: AsyncSession, comment_id: int):
    result = await db.execute(
        select(Comment)
        .where(Comment.id == comment_id)
    )
    return result.scalars().first()


async def delete_comment_admin(
        db: AsyncSession,
        comment_id: int
):
    comment = await get_comment(db, comment_id)
    if comment:
        await db.delete(comment)
        await db.commit()
    return comment
