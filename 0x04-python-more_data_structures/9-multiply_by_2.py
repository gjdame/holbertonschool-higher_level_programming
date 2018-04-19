#!/usr/bin/python3


def multiply_by_2(a_dictionary):

    new_dictionary = dict()

    for key in a_dictionary:
        new_dictionary[key] = a_dictionary[key] * 2

    return(new_dictionary)
