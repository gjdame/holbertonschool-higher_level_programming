#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    if idx < 0 or idx >= len(my_list):
        new_list = my_list.copy()
        return(new_list)
    new_list = my_list.copy()
    new_list.insert(idx, element)
    del new_list[idx + 1]
    return(new_list)
