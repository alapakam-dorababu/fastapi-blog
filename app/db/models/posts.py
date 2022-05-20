from sqlalchemy import Column, Integer, String, Boolean

from app.db.databases import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    publish = Column(Boolean, default=True)
