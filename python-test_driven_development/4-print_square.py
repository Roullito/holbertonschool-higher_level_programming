#!/usr/bin/python3
"""Module for print_square function.
Prints a square made of # characters.
Validates the input type and value.
Raises TypeError or ValueError when needed.
No imports allowed."""


def print_square(size):
    """Prints a square of given size using #.
    Size must be a non-negative integer.
    Raises exceptions on invalid input."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
