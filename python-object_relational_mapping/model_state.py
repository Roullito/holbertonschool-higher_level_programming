from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State class for representing states in the database.

    This class maps to the 'states' table in the database using SQLAlchemy ORM.
    It inherits from the SQLAlchemy declarative base class.

    Attributes:
        id (int): The unique identifier for a state.
                  Auto-increments and acts as the primary key.
        name (str): The name of the state. Limited to 128 characters.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
