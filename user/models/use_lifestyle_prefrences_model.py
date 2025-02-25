from sqlalchemy import Column, BigInteger, Date, Integer, String, Bool, Float
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class LifestylePreferences(Base):
    __tablename__ = "lifestyle_preferences"
    __table_args__ = {"extend_existing": True}
    id = Column("index", BigInteger, primary=True, index=True)
    user_id = Column(String)
    cooking_habits = Column(String)
    smoking_habits = Column(String)
    pet_ownership = Column(String)
    typical_sleep_schedule = Column(String)
    cleanliness = Column(String)
    guest_policy = Column(String)
    noise_tolerance = Column(String)
    work_from_home_frequency = Column(String)
    study_from_home_frequency = Column(String)
    work_schedule = Column(String)
    age_range_of_preferred_co_renters = Column(String)
    utility_sharing_preferences = Column(String)
    preferred_gender_of_co_renters = Column(String)
    shared_space_expectations = Column(String)
    created_at = (Date)
    updated_at = Column(Date)
    deleted_at = Column(Date)

    