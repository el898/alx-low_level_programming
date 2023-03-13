#!/usr/bin/python3
#2-replace_in_list.py

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        i = 0
        while i < len(my_list):
            if i == idx:
                my_list[i] = element
                break
            i += 1
        return my_list
