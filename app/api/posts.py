from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.db.databases import get_db
from app.db.models.posts import Post
from app.schemas.post import PostSchema, PostCreateSchema
from app.utils.auth import is_authenticated

router = APIRouter()


@router.get("/posts", response_model=List[PostSchema])
def get_posts(db: Session = Depends(get_db), user: int = Depends(is_authenticated)):
    qs = db.query(Post).all()
    return qs


@router.post("/posts", response_model=PostSchema)
def create_post(
    post: PostCreateSchema,
    db: Session = Depends(get_db),
    user: int = Depends(is_authenticated),
):
    new_post = Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
