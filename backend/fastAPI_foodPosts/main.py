from fastapi import FastAPI
from database import engine, Base
from routes import router

app = FastAPI()

# Initialize the database
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Include router
app.include_router(router)