#!/usr/bin/python3
"""
This module is a custom serialization function for obj
"""

def class_to_json(obj):
    """
    Generates a dictionary representation of an object

    Args:
        obj: instance of a class

    Returns:
        The dictionary
    """
    # Dictionary to store serialized attributes
    serialized_dict = {}

    # Get the instance variables using __dict__
    instance_vars = obj.__dict__

    # Iterate over all attributes of the object
    for attr_name, attr_value in instance_vars.items():
        # Check if the attribute is serializable
        if isinstance(attr_value, (list, dict, str, int, bool)):
            # Add the attribute to the serialized dictionary
            serialized_dict[attr_name] = attr_value

    return serialized_dict

