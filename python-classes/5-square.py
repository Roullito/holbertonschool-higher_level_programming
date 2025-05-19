#!/usr/bin/python3
"""Module 5-square
Defines a Square class that prints itself with '#'.
"""


class Square:
    """Represents a square that can be printed."""

    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size with validation.

        Args:
            value (int): Size value to set.

        Raises:
            TypeError: If value is not int.
            ValueError: If value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate area of square.

        Returns:
            int: Area (size ** 2)
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with '#' or empty line if size is 0.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
