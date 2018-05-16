#!/usr/bin/python3


def write_file(filename="", text=''):
    """write to a file
    Args
        filename - write to this
        text - text to write
    """
    with open(filename, 'w', encoding='UTF8') as f:
        x = f.write(text)
        return(x)
