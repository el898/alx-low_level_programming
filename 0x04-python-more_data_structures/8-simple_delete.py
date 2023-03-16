#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key-value pair from a dictionary.

    Arguments:
    a_dictionary -- the dictionary to be modified
    key -- the key to be deleted (a string, defaults to "")

    Returns:
    The updated dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
