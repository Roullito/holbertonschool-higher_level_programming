#!/usr/bin/python3
"""Module that defines BaseGeometry class with area and integer validator."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Placeholder method for area computation.
        To be implemented by subclasses."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a strictly positive integer.

        Args:
            name (str): the name of the value (for the error message)
            value (int): the value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
