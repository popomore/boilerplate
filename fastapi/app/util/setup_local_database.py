from app.config.settings import settings
from app.dal.schema.base import Base
from app.util.database_client import database_client
from app.util.enum.server_env import ServerEnv


async def setup_local_database():
    if settings.env != ServerEnv.LOCAL:
        return

    async with database_client.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
