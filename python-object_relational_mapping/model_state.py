#!/usr/bin/python3
"""Defines the State class mapped to the table 'states' in the database."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.

    Attributes:
        id (int): The state's id (primary key).
        name (str): The state's name (max 128 chars).
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
