#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list:
        x = len(my_list)
        for x in range(x, 0, -1):
            print("{:d}".format(my_list[x - 1]))
