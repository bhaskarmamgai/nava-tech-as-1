from fastapi import FastAPI
from decouple import config
from routes import members, organizations
from organizations.db import create_master_db

orgApp = FastAPI(title="Organization Management System")

ENV_NAME = config("ENV_NAME", default="development")

orgApp.include_router(organizations.router, prefix="/orgnizations", tags=["Organization"])
orgApp.include_router(members.router, prefix="/members", tags=["Members (Role -> Admin/Staff/SuperUser)"])

@orgApp.on_event("startup")
async def startup():
    create_master_db()
