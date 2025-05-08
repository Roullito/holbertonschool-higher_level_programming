#!/usr/bin/python3
"""
Script that adds all command-line arguments passed to it.

Usage:
    ./3-infinite_add.py arg1 arg2 arg3 ...
Each argument is expected to be an integer.
"""
import sys

if __name__ == "__main__":
    add_number = 0
    for i in range(1, len(sys.argv)):
        add_number += int(sys.argv[i])
    print("{}".format(add_number))
