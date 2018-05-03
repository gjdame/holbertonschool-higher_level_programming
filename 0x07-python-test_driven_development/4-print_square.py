#!/usr/bin/python3


def print_square(size):
    """prints square of size'
    Args:
        size: first name
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise TypeError('size must be >= 0')
    else:
        for i in range(size):
            print('#' * size)
