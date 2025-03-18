from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from typing import List
from schemas import PostCreate, Post, CommentCreate, Comment, LikeCreate
from crud import create_post, get_posts, create_comment, get_comments, create_like

router = APIRouter()

# Route to create a post
@router.post("/posts/", response_model=Post)
async def create_post_route(post: PostCreate, db: AsyncSession = Depends(get_db)):
    return await create_post(db, post)

# Route to read all posts
@router.get("/posts/", response_model=List[Post])
async def get_posts_route(db: AsyncSession = Depends(get_db)):
    return await get_posts(db)

# Route to create a comment
@router.post("/comments/", response_model=Comment)
async def create_comment_route(comment: CommentCreate, db: AsyncSession = Depends(get_db)):
    return await create_comment(db, comment)

# Route to read comments for a post
@router.get("/comments/{post_id}", response_model=List[Comment])
async def get_comments_route(post_id: int, db: AsyncSession = Depends(get_db)):
    return await get_comments(db, post_id)

# Route to create a like
@router.post("/likes/", response_model=LikeCreate)
async def create_like_route(like: LikeCreate, db: AsyncSession = Depends(get_db)):
    return await create_like(db, like)
