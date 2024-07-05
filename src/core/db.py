import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import MetaData
from dotenv import load_dotenv
from src.core.config import settings

load_dotenv()

DATABASE_URL = os.getenv("POSTGRESQL_URI")


engine = create_async_engine(DATABASE_URL, echo=True)
metadata = MetaData()

async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
