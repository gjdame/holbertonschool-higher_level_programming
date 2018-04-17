#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if idx < 0 or idx >= len(my_list):
        return(None)
    new_list = my_list.copy()
    new_list.insert(idx, element)
    del new_list[idx + 1]
    return(new_list)
