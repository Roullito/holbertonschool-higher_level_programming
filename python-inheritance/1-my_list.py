#!/usr/bin/python3
"""Module that defines a custom list class with sorted print functionality."""


class MyList(list):
    """A custom list class that inherits from built-in list
    and can print itself sorted in ascending order.
    """

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
