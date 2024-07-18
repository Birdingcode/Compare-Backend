from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import date


class BalanceSheetBase(BaseModel):
    symbol: str  # This remains required as it's the primary key
    date: Optional[date] = None
    reported_currency: Optional[str] = None
    cik: Optional[str] = None
    filling_date: Optional[date] = None
    accepted_date: Optional[str] = None
    calendar_year: Optional[int] = None
    period: Optional[str] = None
    cash_and_cash_equivalents: Optional[int] = None
    short_term_investments: Optional[int] = None
    cash_and_short_term_investments: Optional[int] = None
    net_receivables: Optional[int] = None
    inventory: Optional[int] = None
    other_current_assets: Optional[int] = None
    total_current_assets: Optional[int] = None
    property_plant_equipment_net: Optional[int] = None
    goodwill: Optional[int] = None
    intangible_assets: Optional[int] = None
    goodwill_and_intangible_assets: Optional[int] = None
    long_term_investments: Optional[int] = None
    tax_assets: Optional[int] = None
    other_non_current_assets: Optional[int] = None
    total_non_current_assets: Optional[int] = None
    other_assets: Optional[int] = None
    total_assets: Optional[int] = None
    account_payables: Optional[int] = None
    short_term_debt: Optional[int] = None
    tax_payables: Optional[int] = None
    deferred_revenue: Optional[int] = None
    other_current_liabilities: Optional[int] = None
    total_current_liabilities: Optional[int] = None
    long_term_debt: Optional[int] = None
    deferred_revenue_non_current: Optional[int] = None
    deferred_tax_liabilities_non_current: Optional[int] = None
    other_non_current_liabilities: Optional[int] = None
    total_non_current_liabilities: Optional[int] = None
    other_liabilities: Optional[int] = None
    capital_lease_obligations: Optional[int] = None
    total_liabilities: Optional[int] = None
    preferred_stock: Optional[int] = None
    common_stock: Optional[int] = None
    retained_earnings: Optional[int] = None
    accumulated_other_comprehensive_income_loss: Optional[int] = None
    other_total_stockholders_equity: Optional[int] = None
    total_stockholders_equity: Optional[int] = None
    total_equity: Optional[int] = None
    total_liabilities_and_stockholders_equity: Optional[int] = None
    minority_interest: Optional[int] = None
    total_liabilities_and_total_equity: Optional[int] = None
    total_investments: Optional[int] = None
    total_debt: Optional[int] = None
    net_debt: Optional[int] = None


class BalanceSheetCreate(BalanceSheetBase):
    symbol: str
    date: date
    reported_currency: str = Field(...,alias="reportedCurrency")
    cik: str
    filling_date: date = Field(...,alias="fillingDate")
    accepted_date: str = Field(...,alias="acceptedDate")
    calendar_year: int = Field(..., alias="calendarYear")
    period: str
    cash_and_cash_equivalents: int = Field(...,alias="cashAndCashEquivalents")
    short_term_investments: int = Field(...,alias="shortTermInvestments")
    cash_and_short_term_investments: int = Field(...,alias="cashAndShortTermInvestments")
    net_receivables: int = Field(...,alias="netReceivables")
    inventory: int
    other_current_assets: int = Field(...,alias="otherCurrentAssets")
    total_current_assets: int = Field(...,alias="totalCurrentAssets")
    property_plant_equipment_net: int = Field(...,alias="propertyPlantEquipmentNet")
    goodwill: int
    intangible_assets: int = Field(...,alias="intangibleAssets")
    goodwill_and_intangible_assets: int = Field(...,alias="goodwillAndIntangibleAssets")
    long_term_investments: int = Field(...,alias="longTermInvestments")
    tax_assets: int = Field(...,alias="taxAssets")
    other_non_current_assets: int = Field(...,alias="otherNonCurrentAssets")
    total_non_current_assets: int = Field(...,alias="totalNonCurrentAssets")
    other_assets: int = Field(...,alias="otherAssets")
    total_assets: int = Field(...,alias="totalAssets")
    account_payables: int = Field(...,alias="accountPayables")
    short_term_debt: int = Field(...,alias="shortTermDebt")
    tax_payables: int = Field(...,alias="taxPayables")
    deferred_revenue: int = Field(...,alias="deferredRevenue")
    other_current_liabilities: int = Field(...,alias="otherCurrentLiabilities")
    total_current_liabilities: int = Field(...,alias="totalCurrentLiabilities")
    long_term_debt: int = Field(...,alias="longTermDebt")
    deferred_revenue_non_current: int = Field(...,alias="deferredRevenueNonCurrent")
    deferred_tax_liabilities_non_current: int = Field(...,alias="deferredTaxLiabilitiesNonCurrent")
    other_non_current_liabilities: int = Field(...,alias="otherNonCurrentLiabilities")
    total_non_current_liabilities: int = Field(...,alias="totalNonCurrentLiabilities")
    other_liabilities: int = Field(...,alias="otherLiabilities")
    capital_lease_obligations: int = Field(...,alias="capitalLeaseObligations")
    total_liabilities: int = Field(...,alias="totalLiabilities")
    preferred_stock: int = Field(...,alias="preferredStock")
    common_stock: int = Field(...,alias="commonStock")
    retained_earnings: int = Field(...,alias="retainedEarnings")
    accumulated_other_comprehensive_income_loss: int = Field(...,alias="accumulatedOtherComprehensiveIncomeLoss")
    other_total_stockholders_equity: int = Field(...,alias="othertotalStockholdersEquity")
    total_stockholders_equity: int = Field(...,alias="totalStockholdersEquity")
    total_equity: int = Field(...,alias="totalEquity")
    total_liabilities_and_stockholders_equity: int = Field(...,alias="totalLiabilitiesAndStockholdersEquity")
    minority_interest: int = Field(...,alias="minorityInterest")
    total_liabilities_and_total_equity: int = Field(...,alias="totalLiabilitiesAndTotalEquity")
    total_investments: int = Field(...,alias="totalInvestments")
    total_debt: int = Field(...,alias="totalDebt")
    net_debt: int = Field(...,alias="netDebt")


class BalanceSheetUpdate(BalanceSheetBase):
    pass


class BalanceSheet(BalanceSheetCreate):
    model_config = ConfigDict(from_attributes=True,populate_by_name=True)


class BalanceSheetInDB(BalanceSheet):
    pass
