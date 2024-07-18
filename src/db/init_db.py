from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import Base, engine
from src.models import balance_sheet


async def init_db(db: AsyncSession) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)