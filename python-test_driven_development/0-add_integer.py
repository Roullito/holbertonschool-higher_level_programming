#!/usr/bin/python3
"""
Module for add_integer function.
Adds two numbers, casting floats to ints.
Raises TypeError if inputs are invalid.
"""


def add_integer(a, b=98):
    """
    Add two numbers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
