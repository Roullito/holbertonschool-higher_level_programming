#!/usr/bin/python3
"""Module 4-square
Defines a Square class with getter and setter for size.
"""


class Square:
    """
    Represents a square with encapsulated size.
    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.
        Args:
            size (int): The size of the square (default is 0).
        """

        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.
        Returns:
            int: The size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.
        Args:
            value (int): The new size.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.
        Returns:
            int: The area of the square.
        """

        return self.__size ** 2
