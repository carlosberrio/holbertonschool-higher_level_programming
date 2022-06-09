#!/usr/bin/python3
"""contains json functions import"""
from json import dumps


def to_json_string(my_obj):
    """Write a function that returns the JSON"""
    return dumps(my_obj)
