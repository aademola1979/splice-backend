from sqlalchemy import Column, BigInteger, Date, Integer, String, Bool, Float
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Zone(Base):
    __tablename__ = "zone"
    __table_args__ = {"extend_existing": True}
    id = Column("index", BigInteger, primary=True)
    code = Column(String)
    name = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)