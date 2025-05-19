#!/usr/bin/python3
"""Module 1-square
Defines a Square class with private size attribute.
"""


class Square:
    """
    Represents a square with a private size.
    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.
        Args:
            size (int): The size of the square.
        """

        self.__size = size
