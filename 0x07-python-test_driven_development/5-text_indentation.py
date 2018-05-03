#!/usr/bin/python3


def text_indentation(text):
    """prtins text with 2 new lines after each '.' '?' or ':'
    Args:
        text: string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        for c in text:
            if c is '.' or c is '?' or c is ':':
                print("{:s}\n".format(c))
            else:
                print("{:s}".format(c), end="")
