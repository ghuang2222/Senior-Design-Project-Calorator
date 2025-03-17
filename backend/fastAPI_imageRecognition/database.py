from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

DATABASE_URL = "postgresql+asyncpg://myuser:mypassword@localhost/food_db"

# Create the database engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Declare a base for models
Base = declarative_base()

# Session maker for interacting with the database
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session