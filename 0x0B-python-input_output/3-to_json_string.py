#!/usr/bin/python3
"""
This module contains a function that returns the JSON
representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Function to return the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to a JSON string.

    Returns:
        str: The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
