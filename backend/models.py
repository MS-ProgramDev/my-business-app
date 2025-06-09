from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BusinessProfile(Base):
    __tablename__ = 'business_profiles'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    area = Column(Integer)
    seating_capacity = Column(Integer)
    uses_gas = Column(Boolean)
    serves_meat = Column(Boolean)
    offers_delivery = Column(Boolean)
    serves_alcohol = Column(Boolean)

class Requirement(Base):
    __tablename__ = 'requirements'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    action = Column(Text)
    priority = Column(String)

class RequirementCondition(Base):
    __tablename__ = 'requirement_conditions'
    id = Column(Integer, primary_key=True)
    requirement_id = Column(Integer, ForeignKey('requirements.id'))
    field_name = Column(String)
    operator = Column(String)
    value = Column(String)
