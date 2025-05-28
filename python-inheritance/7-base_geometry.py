#!/usr/bin/python3
"""Module that defines BaseGeometry class with validation and area method."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): the name of the value.
            value (int): the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
