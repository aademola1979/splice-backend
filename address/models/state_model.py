from sqlalchemy import Column, BigInteger, Date, Integer, String, Bool, Float
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class _State(Base):
    __tablename__ = "_state"
    __table_args__ = {"extend_existing": True}
    id = Column("index", BigInteger, primary_key=True)
    name = Column(String)
    zone_id = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)
    deleted_at = Column(Date)
