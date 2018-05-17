#!/usr/bin/python3


def add_attribute(obj, attr, value):
    """add attribute if possible
    Args
       obj
       name
       value
    Return: error if not possible
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError('can\'t add new attribute')
    setattr(obj, attr, value)
