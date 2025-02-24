from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas import UserCreate, UserResponse
from crud import create_user, get_user_by_username
from auth import verify_password, create_access_token, verify_access_token
from datetime import timedelta

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return await create_user(db, user)

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    db_user = await get_user_by_username(db, form_data.username)
    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Create access token
    access_toke = create_access_token(
        data={sub: db_user.username},
        expires_delta=timedelta(minutes=30)
    )

@router.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    payload = verify_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    username: str = payload.get("sub")
    user = await get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return {"message": f"Hello, {user.username}! YOu have accessed a protected route."}