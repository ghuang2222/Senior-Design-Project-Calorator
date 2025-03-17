from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import FoodInfo

async def get_food_info(db: AsyncSession, label: str):
    result = await db.execute(select(FoodInfo).filter(FoodInfo.label == label))
    return result.scalars().first()
