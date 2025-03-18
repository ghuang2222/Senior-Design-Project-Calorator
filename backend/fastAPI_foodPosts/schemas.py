from pydantic import BaseModel

class PostBase(BaseModel):
    image_url: str
    description: Optional[str] = None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    post_id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class LikeBase(BaseModel):
    post_id: int
    user_id: int

class Like(LikeBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True