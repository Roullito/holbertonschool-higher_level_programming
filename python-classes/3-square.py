#!/usr/bin/python3
"""Module 3-square
Defines a Square class with area calculation.
"""


class Square:
    """
    Represents a square with size and area calculation.
    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.
        Args:
            size (int): The size of the square (default is 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.
        Returns:
            int: The area of the square.
        """

        return self.__size ** 2
