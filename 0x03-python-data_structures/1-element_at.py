#!/bin/bash
def element_at(my_list, idx):
    """get ele from lst."""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
