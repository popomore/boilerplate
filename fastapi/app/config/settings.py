import logging
import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings

from app.util.enum.server_env import ServerEnv


class DatabaseConfig(BaseModel):
    url: str
    pool_pre_ping: bool = True
    pool_size: int = 200
    max_overflow: int = 200
    pool_recycle: int = 200
    pool_timeout: int = 10


logger = logging.getLogger(__name__)
project_dir: str = os.path.abspath(os.path.join(__file__, "../../.."))
server_home = os.getenv("HOME", "/home/admin")
env = ServerEnv(os.getenv("SERVER_ENV", "local"))


class Settings(BaseSettings):
    appname: str = "fastapi"
    project_dir: str = project_dir
    server_home: str = server_home
    env: ServerEnv = env

    # database
    database: DatabaseConfig = DatabaseConfig(
        url="postgresql+asyncpg://root:root@localhost:5432/fastapi"
    )


settings = Settings()
