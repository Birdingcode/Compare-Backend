import httpx, os
from typing import Dict, Any
from dotenv import load_dotenv
from fastapi import HTTPException
from fastapi.logger import logger

load_dotenv()

FMP_BASE_URL = os.getenv("FMP_BASE_URL_V3")
FMP_API_KEY = os.getenv("FMP_API_KEY")


class FMPService:
    #Temporary annual period
    @staticmethod
    async def get_financial_statement(symbol: str, statement_type: str) -> Dict[str, Any]:
        url = f"{FMP_BASE_URL}/{statement_type}/{symbol}?period=annual&apikey={FMP_API_KEY}"
        print(url)
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code == 200:
                data = response.json()
                if data:
                    return data  # Assuming the most recent statement is first
            raise HTTPException(status_code=response.status_code, detail=f"Failed to fetch {statement_type.capitalize()} for {symbol}")


fmp_service = FMPService()
