from fastapi import FastAPI


from app.db.databases import engine
from app.db.models.base import Base

# all api routes
from app.routers import api_routers


# Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API", description="This is simple blog api")
app.include_router(api_routers)
