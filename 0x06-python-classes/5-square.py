#!/usr/bin/python3


class Square:
    """ creates a square and determines area and prints"""
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

    def my_print(self):
        """prints square of size with # symbol"""
        for i in range(self.__size):
            print('#' * self.__size, end='')
            print('')
        if self.__size == 0:
            print('')
