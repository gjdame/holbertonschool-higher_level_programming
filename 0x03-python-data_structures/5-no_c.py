#!/usr/bin/python3


def no_c(my_string):
    my_string = [i for i in my_string if i.upper() != 'C']
    my_string = ''.join(my_string)
    return (my_string)
