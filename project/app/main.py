# project/app/main.py


import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api import ping
from app.db import init_db

def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)

    return application


app = create_application()

init_db(app)