from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True  # This ensures this class is not created as a table

    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary Key
    created_at = Column(DateTime, default=func.now(), nullable=False)
    modified_at = Column(DateTime, default=func.now(), nullable=False)

    # def save(self, session):
    #     """Save the instance to the database."""
    #     session.add(self)
    #     session.commit()
    #
    # def delete(self, session):
    #     """Delete the instance from the database."""
    #     session.delete(self)
    #     session.commit()