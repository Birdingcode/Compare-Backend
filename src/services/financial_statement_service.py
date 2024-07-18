import logging, json
from typing import List, Dict, Any, Union, Type
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.balance_sheet import BalanceSheet
from pydantic import ValidationError

# from src.schemas.income_statement import IncomeStatement
# from src.schemas.cash_flow_statement import CashFlowStatement

logger = logging.getLogger(__name__)
StatementType = Union[BalanceSheet]


class FinancialStatementService:
    async def get_statements(self, db: AsyncSession, symbol: str, statement_type: str) -> List[StatementType]:
        query = text("""
            SELECT * FROM {table_name}
            WHERE symbol = :symbol
            ORDER BY date DESC
        """.format(table_name=self._get_table_name(statement_type)))

        result = await db.execute(query, {"symbol": symbol})
        return [self._get_schema(statement_type).from_orm(row) for row in result.fetchall()]

    # async def create_or_update_statements(self, db: AsyncSession, statements: List[Dict[str, Any]],statement_type: str) -> List[StatementType]:
    #     table_name = self._get_table_name(statement_type)
    #     schema = self._get_schema(statement_type)
    #
    #     results = []
    #     for statement_data in statements:
    #         # Use your existing schema to parse the raw data
    #         statement = schema(**statement_data)
    #
    #         query = text(f"""
    #             INSERT INTO {table_name} ({', '.join(statement.dict().keys())})
    #             VALUES ({', '.join([f':{k}' for k in statement.dict().keys()])})
    #             ON CONFLICT (symbol, calendar_year, period)
    #             DO NOTHING
    #             RETURNING *
    #         """)
    #
    #         result = await db.execute(query, statement.dict())
    #         inserted_row = result.fetchone()
    #
    #         if inserted_row:
    #             results.append(schema.from_orm(inserted_row))
    #         else:
    #             # If no insert occurred, fetch the existing record
    #             existing_query = text(f"""
    #                 SELECT * FROM {table_name}
    #                 WHERE symbol = :symbol
    #                 AND calendar_year = :calendar_year
    #                 AND period = :period
    #             """)
    #             existing_result = await db.execute(existing_query, {
    #                 "symbol": statement.symbol,
    #                 "calendar_year": statement.calendar_year,
    #                 "period": statement.period
    #             })
    #             existing_row = existing_result.fetchone()
    #             if existing_row:
    #                 results.append(schema.from_orm(existing_row))
    #
    #     await db.commit()
    #     return results

    async def create_or_update_statements(self, db: AsyncSession, statements: List[Dict[str, Any]],statement_type: str) -> List[StatementType]:
        table_name = self._get_table_name(statement_type)
        schema = self._get_schema(statement_type)

        results = []
        for index, statement_data in enumerate(statements):
            try:
                print(statement_data)

                # Use your existing schema to parse the raw data
                statement = schema(**statement_data)

                query = text(f"""
                    INSERT INTO {table_name} ({', '.join(statement.dict().keys())})
                    VALUES ({', '.join([f':{k}' for k in statement.dict().keys()])})
                    ON CONFLICT (symbol, calendar_year, period) 
                    DO NOTHING
                    RETURNING *
                """)

                try:
                    result = await db.execute(query, statement.dict())
                    inserted_row = result.fetchone()

                    if inserted_row:
                        results.append(schema.from_orm(inserted_row))
                        logger.info(
                            f"Inserted new {statement_type} for symbol {statement.symbol}, year {statement.calendar_year}, period {statement.period}")
                    else:
                        # If no insert occurred, fetch the existing record
                        existing_query = text(f"""
                            SELECT * FROM {table_name}
                            WHERE symbol = :symbol 
                            AND calendar_year = :calendar_year 
                            AND period = :period
                        """)
                        existing_result = await db.execute(existing_query, {
                            "symbol": statement.symbol,
                            "calendar_year": statement.calendar_year,
                            "period": statement.period
                        })
                        existing_row = existing_result.fetchone()
                        if existing_row:
                            results.append(schema.from_orm(existing_row))
                            logger.info(
                                f"Found existing {statement_type} for symbol {statement.symbol}, year {statement.calendar_year}, period {statement.period}")
                        else:
                            logger.warning(
                                f"No {statement_type} found for symbol {statement.symbol}, year {statement.calendar_year}, period {statement.period}")

                except SQLAlchemyError as e:
                    logger.error(f"Database error while processing {statement_type} for index {index}: {str(e)}")
                    # You might want to raise this error or handle it differently
                    raise

            except ValidationError as e:
                logger.error(f"Validation error for {statement_type} data at index {index}: {str(e)}")
                # You might want to skip this item or handle the error differently
                continue

            except Exception as e:
                logger.error(f"Unexpected error processing {statement_type} data at index {index}: {str(e)}")
                # You might want to raise this error or handle it differently
                raise

        try:
            await db.commit()
            logger.info(f"Successfully committed {len(results)} {statement_type} statements to the database")
        except SQLAlchemyError as e:
            logger.error(f"Error committing {statement_type} statements to the database: {str(e)}")
            await db.rollback()
            raise

        return results

    @staticmethod
    def _get_table_name(statement_type: str) -> str:
        if statement_type == "balance-sheet-statement":
            return "balance_sheets"
        # elif statement_type == "income-statement":
        #     return "income_statements"
        # elif statement_type == "cash-flow-statement":
        #     return "cash_flow_statements"
        else:
            raise ValueError(f"Unknown statement type: {statement_type}")

    @staticmethod
    def _get_schema(statement_type: str) -> Type[StatementType]:
        if statement_type == "balance-sheet-statement":
            return BalanceSheet
        # elif statement_type == "income-statement":
        #     return IncomeStatement
        # elif statement_type == "cash-flow-statement":
        #     return CashFlowStatement
        else:
            raise ValueError(f"Unknown statement type: {statement_type}")


financial_statement_service = FinancialStatementService()
