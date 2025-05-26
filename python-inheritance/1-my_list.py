#!/usr/bin/python3
"""Module that defines MyList class inheriting from built-in list."""


class MyList(list):
    """Custom list class that can print itself sorted."""

    def print_sorted(self):
        """Print the list elements sorted in ascending order (non-modifying)"""
        print(sorted(self))
