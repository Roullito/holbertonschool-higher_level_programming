#!/usr/bin/python3
"""Module 6-square
Defines a Square class with size and position, and prints the square visually.
"""


class Square:
    class Square:
        """
        Represents a square with a given size and position.
        Attributes:
            __size (int): The size of the square (private).
            __position (tuple): The (x, y) position for printing (private).
        """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.
        Args:
            size (int): The size of the square (default 0).
            position (tuple): The position offset as a tuple of two positive integers.
        """

        self.size = size
        self.position = position

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
        Set the size of the square.
        Args:
            value (int): The new size value.

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

    def my_print(self):
        """
        Print the square using the `#` character,
        offset by the `position` attribute.
        If size is 0, prints an empty line.
        """
        
        for i in range(self.__position[1]):
            print()
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(n, int) for n in value)
            or not all(n >= 0 for n in value)):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
