#!/usr/bin/python3
"""
contains writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """unction that writes a string to a text file (UTF8) and returns the
    number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
