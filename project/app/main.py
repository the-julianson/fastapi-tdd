# project/app/main.py


from app.api import ping
from app.db import init_db
from fastapi import FastAPI


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)

    return application


app = create_application()

init_db(app)
