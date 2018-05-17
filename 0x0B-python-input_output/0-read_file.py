#!/usr/bin/python3


def read_file(filename=""):
    """open and read a file
    Args
       filename
    """
    with open(filename, encoding='UTF8') as f:
        text = f.read()
        print(text, end='')
