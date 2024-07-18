from sqlalchemy import Integer, String, Date, BigInteger, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from src.db.session import Base


class BalanceSheet(Base):
    __tablename__ = "balance_sheets"

    symbol: Mapped[str] = mapped_column(String(10), primary_key=True)
    calendar_year: Mapped[int] = mapped_column(Integer, primary_key=True)
    period: Mapped[str] = mapped_column(String(2), primary_key=True)

    date: Mapped[date] = mapped_column(Date)
    reported_currency: Mapped[str] = mapped_column(String(3))
    cik: Mapped[str] = mapped_column(String(10))
    filling_date: Mapped[date] = mapped_column(Date)
    accepted_date: Mapped[str] = mapped_column(String(25))
    cash_and_cash_equivalents: Mapped[BigInteger] = mapped_column(BigInteger)
    short_term_investments: Mapped[BigInteger] = mapped_column(BigInteger)
    cash_and_short_term_investments: Mapped[BigInteger] = mapped_column(BigInteger)
    net_receivables: Mapped[BigInteger] = mapped_column(BigInteger)
    inventory: Mapped[BigInteger] = mapped_column(BigInteger)
    other_current_assets: Mapped[BigInteger] = mapped_column(BigInteger)
    total_current_assets: Mapped[BigInteger] = mapped_column(BigInteger)
    property_plant_equipment_net: Mapped[BigInteger] = mapped_column(BigInteger)
    goodwill: Mapped[BigInteger] = mapped_column(BigInteger)
    intangible_assets: Mapped[BigInteger] = mapped_column(BigInteger)
    goodwill_and_intangible_assets: Mapped[BigInteger] = mapped_column(BigInteger)
    long_term_investments: Mapped[BigInteger] = mapped_column(BigInteger)
    tax_assets: Mapped[BigInteger] = mapped_column(BigInteger)
    other_non_current_assets: Mapped[BigInteger] = mapped_column(BigInteger)
    total_non_current_assets: Mapped[BigInteger] = mapped_column(BigInteger)
    other_assets: Mapped[BigInteger] = mapped_column(BigInteger)
    total_assets: Mapped[BigInteger] = mapped_column(BigInteger)
    account_payables: Mapped[BigInteger] = mapped_column(BigInteger)
    short_term_debt: Mapped[BigInteger] = mapped_column(BigInteger)
    tax_payables: Mapped[BigInteger] = mapped_column(BigInteger)
    deferred_revenue: Mapped[BigInteger] = mapped_column(BigInteger)
    other_current_liabilities: Mapped[BigInteger] = mapped_column(BigInteger)
    total_current_liabilities: Mapped[BigInteger] = mapped_column(BigInteger)
    long_term_debt: Mapped[BigInteger] = mapped_column(BigInteger)
    deferred_revenue_non_current: Mapped[BigInteger] = mapped_column(BigInteger)
    deferred_tax_liabilities_non_current: Mapped[BigInteger] = mapped_column(BigInteger)
    other_non_current_liabilities: Mapped[BigInteger] = mapped_column(BigInteger)
    total_non_current_liabilities: Mapped[BigInteger] = mapped_column(BigInteger)
    other_liabilities: Mapped[BigInteger] = mapped_column(BigInteger)
    capital_lease_obligations: Mapped[BigInteger] = mapped_column(BigInteger)
    total_liabilities: Mapped[BigInteger] = mapped_column(BigInteger)
    preferred_stock: Mapped[BigInteger] = mapped_column(BigInteger)
    common_stock: Mapped[BigInteger] = mapped_column(BigInteger)
    retained_earnings: Mapped[BigInteger] = mapped_column(BigInteger)
    accumulated_other_comprehensive_income_loss: Mapped[BigInteger] = mapped_column(BigInteger)
    other_total_stockholders_equity: Mapped[BigInteger] = mapped_column(BigInteger)
    total_stockholders_equity: Mapped[BigInteger] = mapped_column(BigInteger)
    total_equity: Mapped[BigInteger] = mapped_column(BigInteger)
    total_liabilities_and_stockholders_equity: Mapped[BigInteger] = mapped_column(BigInteger)
    minority_interest: Mapped[BigInteger] = mapped_column(BigInteger)
    total_liabilities_and_total_equity: Mapped[BigInteger] = mapped_column(BigInteger)
    total_investments: Mapped[BigInteger] = mapped_column(BigInteger)
    total_debt: Mapped[BigInteger] = mapped_column(BigInteger)
    net_debt: Mapped[BigInteger] = mapped_column(BigInteger)

    __table_args__ = (
        PrimaryKeyConstraint('symbol', 'calendar_year', 'period'),
    )

    def __repr__(self):
        return f"<BalanceSheet(symbol={self.symbol}, date={self.date})>"
