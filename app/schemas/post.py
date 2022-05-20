from pydantic import BaseModel


class PostSchema(BaseModel):
    id: int
    title: str
    publish: bool

    class Config:
        orm_mode = True


class PostCreateSchema(BaseModel):
    title: str
    publish: bool
