#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
        Return True if the object is an instance of a subclass of a_class;
        returns False if the object is exactly an instance of a_class or unrelated.

        Args:
            obj: The object to check.
            a_class: The class to compare against.

        Returns:
            True if obj is instance of a subclass of a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
