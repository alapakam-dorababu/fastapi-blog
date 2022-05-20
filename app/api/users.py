from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.db.databases import get_db
from app.db.models.users import User
from app.schemas.users import UserCreateSchema
from app.utils.auth import get_password_hash, authenticate, create_access_token


router = APIRouter()


@router.post("/users", response_model=UserCreateSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    user.password = hashed_password
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/token")
def user_login(
    user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate(db, user.username, user.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Please check authentication credentials",
        )
    access_token = create_access_token(data={"id": user.id})
    return {"access_token": access_token, "token_type": "Bearer"}
