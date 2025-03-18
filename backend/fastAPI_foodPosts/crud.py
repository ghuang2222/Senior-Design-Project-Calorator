from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Post as DBPost, Comment as DBComment, Like as DBLike
from .schemas import PostCreate, CommentCreate, LikeCreate

# Create a Post
async def create_post(db: AsyncSession, post: PostCreate):
    db_post = DBPost(**post.dict())
    db.add(db_post)
    await db.commit()
    await db.refresh(db_post)
    return db_post

# Read all Posts
async def get_posts(db: AsyncSession):
    result = await db.execute(select(DBPost))
    posts = result.scalars().all()
    return posts

# Create a Comment
async def create_comment(db: AsyncSession, comment: CommentCreate):
    db_comment = DBComment(**comment.dict())
    db.add(db_comment)
    await db.commit()
    await db.refresh(db_comment)
    return db_comment

# Read Comments for a Post
async def get_comments(db: AsyncSession, post_id: int):
    result = await db.execute(select(DBComment).filter(DBComment.post_id == post_id))
    comments = result.scalars().all()
    return comments

# Create a Like
async def create_like(db: AsyncSession, like: LikeCreate):
    db_like = DBLike(**like.dict())
    db.add(db_like)
    await db.commit()
    return db_like
