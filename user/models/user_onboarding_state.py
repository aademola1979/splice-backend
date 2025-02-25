from sqlalchemy import Column, BigInteger, Date, Integer, String, Bool, Float
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class OnBoardingState(Base):
    __tablename__ = "onboarding_state"
    __table_args__ = {"extend_existing": True}
    id = Column("index", BigInteger, primary=True, index=True)
    user_id = Column(String)
    current_step_id = Column(String)
    is_complete = Column(Bool)
    created_at = Column(Date)
    updated_at = Column(Date)


    