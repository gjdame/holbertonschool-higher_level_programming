#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """initalizer
        Args
           size: size of side of square
        """
        super().integer_validator('size', size):
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """returns dimension of square"""
        return('[Square] {}/{}'.format(self.__size, self.__size))
