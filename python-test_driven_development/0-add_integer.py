#!/usr/bin/python3
"""
Module for add_integer function.

This module provides a function that adds two integers or floats.
It casts floats to integers before performing the addition.
If the input is not a number, it raises a TypeError.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, casting floats to integers first.

    Args:
        a (int, float): First number.
        b (int, float, optional): Second number (default is 98).

    Returns:
        int: The sum of a and b, both casted to integers.

    Raises:
        TypeError: If a or b is not an int or float.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
        >>> add_integer(4, "School")
        Traceback (most recent call last):
        ...
        TypeError: b must be an integer
        >>> add_integer(None)
        Traceback (most recent call last):
        ...
        TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
