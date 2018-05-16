#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    """read specifc # of lines of a file
    Args
       filename
       nb_lines - number of lines to read
    if nb is less than 0 or greater than file size, returns whole file
    """
    num = 0
    with open(filename, encoding='UTF8') as f:
        for line in f:
            num += 1
    with open(filename, encoding='UTF8') as f:
        if nb_lines <= 0 or nb_lines >= num:
            print(f.read(), end='')
        else:
            for line in range(nb_lines):
                print(f.readline(), end='')
