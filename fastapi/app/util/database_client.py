from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config.settings import settings


class DatabaseClient:
    def __init__(self):
        pass

    def initialize(self):
        self.engine = create_async_engine(
            **settings.database.model_dump(),
        )
        self.sessionmaker = async_sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def close(self):
        if self.engine:
            await self.engine.dispose()

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, Any]:
        session = yield self.sessionmaker()
        try:
            yield session
        except:
            await session.rollback()
            raise
        finally:
            await session.close()


database_client = DatabaseClient()
