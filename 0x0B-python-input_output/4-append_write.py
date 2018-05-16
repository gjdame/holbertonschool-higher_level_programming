#!/usr/bin/python3


def append_write(filename="", text=''):
    """append writing
    Args
       filename
       text
    Return number of lines"""
    with open(filename, 'a', encoding='UTF8') as f:
        x = f.write(text)
        return(x)
