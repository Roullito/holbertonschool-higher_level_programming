#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, "a") as f:
        len_text = f.write(text)
        return len_text
