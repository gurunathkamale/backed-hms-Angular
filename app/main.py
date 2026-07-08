from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.models.user_model import User
from app.core.dbconnection import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()




origins = ["http://localhost:4800"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

Base.metadata.create_all(bind=engine)

app.include_router(user_router)