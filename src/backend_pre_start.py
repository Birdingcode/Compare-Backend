import asyncio
import logging
from fastapi.logger import logger as fastapi_logger
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy import text
from src.db.session import engine
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


max_tries = 10
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(fastapi_logger, logging.INFO),
    after=after_log(fastapi_logger, logging.WARN),
)
async def init(db_engine: AsyncEngine) -> None:
    try:
        async with AsyncSession(db_engine) as session:
            await session.execute(text("SELECT 1"))
        fastapi_logger.info("DB is awake")
    except Exception as e:
        fastapi_logger.error(e)
        raise e


async def main():
    fastapi_logger.info("Initializing DB")
    await init(engine)
    fastapi_logger.info("DB finished initializing")


if __name__ == '__main__':
    print("before main")
    asyncio.run(main())
    print("after main")
