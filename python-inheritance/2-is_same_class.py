#!/usr/bin/python3
"""Module that defines a function to check for exact object class match."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, not a subclass."""
    return type(obj) is a_class
