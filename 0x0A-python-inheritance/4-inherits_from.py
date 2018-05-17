#!/usr/bin/python3


def inherits_from(obj, a_class):
    """returns true if object is an instance of a class inherited from a_class
    Args
        obj: object
        a_class: class
    Return: True or False"""
    if not type(obj) == a_class and issubclass(type(obj), a_class):
        return(True)
    else:
        return(False)
