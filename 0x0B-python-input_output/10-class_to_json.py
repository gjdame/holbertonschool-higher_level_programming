#!/usr/bin/python3
import json


def class_to_json(obj):
    """class to json objects
    returns s
    """
    s = obj.__dict__
    return(s)
