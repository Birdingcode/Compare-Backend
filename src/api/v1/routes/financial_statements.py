from typing import List, Union
from fastapi import APIRouter, Depends, HTTPException
from fastapi.logger import logger
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.fmp_service import fmp_service
from src.services.financial_statement_service import financial_statement_service
from src.api.deps import get_db

from src.schemas import BalanceSheet

router = APIRouter()


@router.get("/{statement_type}/{symbol}", response_model=List[Union[BalanceSheet]])
async def get_financial_statements(statement_type: str, symbol: str, db: AsyncSession = Depends(get_db)):
    statements = await financial_statement_service.get_statements(db, symbol, statement_type)
    if not statements:
        try:
            statement_data = await fmp_service.get_financial_statement(symbol, statement_type)
            statements = await financial_statement_service.create_or_update_statements(db, statement_data, statement_type)
        except Exception as e:
            raise HTTPException(status_code=404, detail=f"{statement_type.capitalize()} for {symbol} not found")

    return statements
