from sqlalchemy import Column, BigInteger, Date, Integer, String, Bool, Float
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class UserFinancialInformation(Base):
    __tablename__ = "user_financial_information"
    __table_args__ = {"extend_existing": True}
    id = Column("index", BigInteger, primary=True, index=True)
    user_id = Column(String)
    annual_rent_budget_range = Column(BigInteger)
    created_at = Column(Date)
    updated_at = Column(Date)