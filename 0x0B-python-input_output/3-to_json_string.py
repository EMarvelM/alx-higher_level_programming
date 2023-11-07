#!/usr/bin/python3
"""This module gets the object representaion of a JSON"""


def to_json_string(my_obj):
    import json
    return json.dumps(my_obj)
