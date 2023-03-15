#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create a new set to store the elements that are present in only one of the sets
    diff_set = set()

    # Iterate over the elements in set_1
    for elem in set_1:
        # If the element is not in set_2, add it to the diff_set
        if elem not in set_2:
            diff_set.add(elem)

    # Iterate over the elements in set_2
    for elem in set_2:
        # If the element is not in set_1, add it to the diff_set
        if elem not in set_1:
            diff_set.add(elem)

    return diff_set
