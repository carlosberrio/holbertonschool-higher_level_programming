#!/usr/bin/python3
"""
contains load
"""
import json


def load_from_json_file(filename):
    """creates an object
    from a json"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
