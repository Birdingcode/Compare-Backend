from fastapi import APIRouter

from src.api.v1.routes import financial_statements

api_router = APIRouter()
api_router.include_router(financial_statements.router,prefix="/financial-statements",tags=["financial-statements"])