#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Adds or updates a key-value pair in a dictionary.

    Arguments:
    a_dictionary -- the dictionary to be updated
    key -- the key to be added or updated (a string)
    value -- the value to be associated with the key (any type)

    Returns:
    The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
