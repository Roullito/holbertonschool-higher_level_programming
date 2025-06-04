#!/usr/bin/env python3
"""
Module task_01_pickle

Provides a class CustomObject that can be serialized to and deserialized
from a file using the pickle module.
Includes:
- Attributes: name (str), age (int), is_student (bool)
- Methods: display(), serialize(), deserialize()
"""

import pickle


class CustomObject:
    """
    CustomObject represents a simple user with basic attributes.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): Name of the object.
            age (int): Age of the object.
            is_student (bool): Whether the object is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the attributes of the object in a readable format.
        """
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """
        Serialize the current instance and save it to a file using pickle.

        Args:
            filename (str): The file path where the object should be saved.
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a file to reconstruct a CustomObject instance.

        Args:
            filename (str): The file path from which to load the object.

        Returns:
            CustomObject or None: The restored object,
            or None if an error occurred.
        """
        try:
            with open(filename, "rb") as f:
                data_restored = pickle.load(f)
            return data_restored
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
