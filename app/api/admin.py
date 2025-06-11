from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from schemas.user import UserRead
from schemas.comment import CommentRead
from services.user import update_user_admin
from services.comment import get_comments, delete_comment_admin
from core.database import get_db
from core.security import get_current_active_admin, get_user_by_uid
from models.user import User

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_current_active_admin)]
)
@router.patch("/users/{user_id}/promote", response_model=UserRead)
async def promote_to_admin(
        user_id: int,
        db: AsyncSession = Depends(get_db)
):
    db_user = await get_user_by_uid(db, user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return await update_user_admin(db, user_id, {"is_admin": True})


@router.delete("/comments/{comment_id}", response_model=CommentRead)
async def admin_delete_comment(
        comment_id: int,
        db: AsyncSession = Depends(get_db)
):
    comment = await get_comments(db, comment_id)
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found"
        )

    await delete_comment_admin(db, comment_id)
    return comment

admin_router = router