#!/usr/bin/python3
"""Module for text_indentation function.
Processes a string and prints it with proper indentation.
Adds two newlines after ., ? or : characters.
Trims leading spaces in the following lines.
Raises TypeError if input is not a string."""


def text_indentation(text):
    """Prints text with two newlines after ., ? or :.
    Removes leading spaces from each new line.
    Raises TypeError if text is not a string."""
    line = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
