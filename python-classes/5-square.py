"""Module 5-square
Defines a Square class with a visual print method.
"""


class Square:
    """
    Represents a square that can be printed using `#`.
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

    def my_print(self):
        """
        Print the square using the `#` character.
        If size is 0, prints an empty line.
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
