#!/usr/bin/python3
"""
contains json string
"""
import json


def from_json_string(my_str):
    """Function load that convert a data type(python) to json string"""
    return json.loads(my_str)
