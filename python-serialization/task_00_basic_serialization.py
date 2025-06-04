#!/usr/bin/env python3
"""
Module task_00_basic_serialization

Provides basic serialization and deserialization functions using JSON format.
Includes:
- serialize_and_save_to_file: saves a dictionary to a JSON file
- load_and_deserialize: loads a dictionary from a JSON file
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the file to save the JSON data.

    Returns:
        None
    """
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file into a Python dictionary.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r") as f:
        obj = json.load(f)
    return obj
