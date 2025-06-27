#!/usr/bin/python3
"""Defines the City class mapped to the table 'cities' in the database."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """Represents a city for a MySQL database.

    Attributes:
        id (int): The city's id (primary key).
        name (str): The city's name (max 128 chars).
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State")
