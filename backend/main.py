from fastapi import FastAPI
from backend.database import Base, engine
from backend.company_module.routes import router as company_router

import backend.models

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(company_router)