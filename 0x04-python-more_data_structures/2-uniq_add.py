#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    sum = 0
    for elem in my_list:
        if elem not in unique_list:
            unique_list.append(elem)
            sum += elem
    return sum
