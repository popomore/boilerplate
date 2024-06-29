from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.util.database_client import database_client
from app.util.setup_local_database import setup_local_database
from app.util.setup_log import setup_log


@asynccontextmanager
async def lifespan(app: FastAPI):
    # init log
    setup_log()
    # init database
    database_client.initialize()
    await setup_local_database()

    # ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎
    # before startup

    yield

    # ⬇︎⬇︎⬇︎⬇︎⬇︎⬇︎⬇︎⬇︎
    # after shutdown

    await database_client.close()
