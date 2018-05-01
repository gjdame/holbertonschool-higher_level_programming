#!/usr/bin/python3


class Square:
    """creates a square and determines area"""
    def __init__(self, size=0):
        """initializes square
        Args:
            size: size of square"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """determines area of square"""
        res = self.__size ** 2
        return(res)

    @property
    def size(self):
        """gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
