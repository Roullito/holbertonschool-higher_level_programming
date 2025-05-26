#!/usr/bin/python3
"""Module that defines BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Placeholder method for area computation.
        To be implemented by subclasses."""
        raise Exception("area() is not implemented")
