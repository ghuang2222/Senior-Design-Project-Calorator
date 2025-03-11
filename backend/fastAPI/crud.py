from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from schemas import UserCreate
from auth import hash_password

async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(username=user.username, hashed_password=hash_password(user.password))
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(User).filter(User.username == username))
    return result.scalars().first()

