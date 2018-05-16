#!/usr/bin/python3


def number_of_lines(filename=""):
    """number of lines
    Args
        filename
    return - num of lines"""
    num = 0
    with open(filename, encoding='UTF8') as f:
        for line in f:
            num += 1
        return(num)
