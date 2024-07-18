from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import AsyncSessionLocal


async def get_db() -> AsyncGenerator[AsyncSession,None]:
    db: AsyncSession | None = None
    try:
        db = AsyncSessionLocal()
        yield db
    finally:
        if db is not None:
            await db.close()
