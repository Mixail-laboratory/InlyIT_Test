from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from schemas.comment import CommentCreate, CommentRead
from services.comment import create_comment, get_comments_by_ad
from core.database import get_db
from core.security import get_current_user
from models.user import User

router = APIRouter(prefix="/ads/{ad_id}/comments", tags=["comments"])


@router.post("/", response_model=CommentRead, status_code=status.HTTP_201_CREATED)
async def add_comment_to_ad(
        ad_id: int,
        comment_data: CommentCreate,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return await create_comment(db, comment_data, ad_id, current_user.id)


@router.get("/", response_model=List[CommentRead])
async def get_ad_comments(
        ad_id: int,
        skip: int = 0,
        limit: int = 100,
        db: AsyncSession = Depends(get_db)
):
    return await get_comments_by_ad(db, ad_id, skip=skip, limit=limit)


comment_router = router
