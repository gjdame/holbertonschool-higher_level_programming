#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        new_list = my_list.copy()
        return(new_list)
    del my_list[idx]
    new_list = my_list.copy()
    return(new_list)
