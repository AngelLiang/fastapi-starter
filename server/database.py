from sqlalchemy.ext.asyncio import (
    AsyncSession, async_sessionmaker, create_async_engine
)
from sqlalchemy.orm import declarative_base, sessionmaker

from server.settings import ASYNC_DATABASE_URL

engine = create_async_engine(ASYNC_DATABASE_URL, echo=False)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


Base = declarative_base()


async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session


async_session = async_sessionmaker(bind=engine, expire_on_commit=False, autoflush=False)
