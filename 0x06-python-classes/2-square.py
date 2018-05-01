#!/usr/bin/python3


class Square:
    """creates a square or area"""
    __size = None

    def __init__(self, size=0):
        """initialize instance of square
        Args:
            size: size of square"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
