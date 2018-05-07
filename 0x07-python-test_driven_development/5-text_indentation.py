#!/usr/bin/python3


def text_indentation(text):
    """prtins text with 2 new lines after each '.' '?' or ':'
    Args:
        text: string
    """
    begin = 0
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i, c in enumerate(text):
        if c in '.?:':
            print(text[begin: i + 1].strip() + '\n')
            begin = i + 1
    if begin < len(text):
        print(text[begin:].strip(), end="")
