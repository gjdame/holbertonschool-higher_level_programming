#!/usr/bin/python3


def add_attribute(obj, name, value):
    """add attribute if possible
    Args
       obj
       name
       value
    Return: error if not possible
    """
    if hasattr(obj, '__slots__'):
        raise TypeErro('can\'t add new attribute')
    if hasattr(obj, '__dict__'):
        obj.name = value
    else:
        raise TypeError('can\'t add new attribute')
