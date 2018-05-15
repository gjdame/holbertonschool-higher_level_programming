#!/usr/bin/python3


def is_same_class(obj, a_class):
    """checks if object is exactly an instance of a_class
    Args
       obj: object
       a_class: class
    """
    return(type(obj) == a_class)
