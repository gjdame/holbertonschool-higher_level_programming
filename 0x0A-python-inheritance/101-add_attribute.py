#!/usr/bin/python3


def add_attribute(obj, name, value):
    """add attribute if possible
    Args
       obj
       name
       value
    Return: error if not possible
    """
    if hasattr(obj, '__slots__') or not hasattr(obj, '__dict__'):
        raise TypeError('can\'t add new attribute')
    if hasattr(obj, name):
        raise TypeError('can\'t add new attribute')
    obj.name = value
