from sqlalchemy import Column, BigInteger, Date, Integer, String, Bool, Float
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class LocalGovernmentAreaModel(Base):
    __tablename__ = "local_government_area"
    __table_args__ = {"extend_existing" : True}
    state_id = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)
    deleted_at = Column(Date)