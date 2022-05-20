from enum import unique
from sqlalchemy import Column, Integer, String, Boolean

from app.db.databases import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, default=True)
    password = Column(String, nullable=False)

    def __str__(self):
        return self.email
