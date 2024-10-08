from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

from core.config import settings

Base = declarative_base()
dsn = (f'postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}@'
       f'{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}')
engine = create_async_engine(dsn, echo=settings.echo, future=True)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
