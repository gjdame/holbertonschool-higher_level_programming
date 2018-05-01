#!/usr/bin/python3


class Square:
    """creats a square or determines area"""
    __size = None

    def __init__(self, size=0):
        """initializes instance of square
        Args:
            size: size of square"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """determines area"""
        res = self.__size * self.__size
        return(res)
