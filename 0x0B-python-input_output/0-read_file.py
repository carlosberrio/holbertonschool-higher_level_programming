#!/usr/bin/python3
"""
CONTAINS THE READ_FILE
"""


def read_file(filename=""):
    """reads a text in utf-8 and prints out"""
    with open(filename, mode="r", encoding="UTF-8") as f:
        print(f.read(), end="")
