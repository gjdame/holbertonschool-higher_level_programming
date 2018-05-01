#!/usr/bin/python3


class Square:
    """initializes square, determines size, calculates area, prints"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes instance of square
        Args:
            size: size of square
            position: position to indent square"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        self.__position = position

    def area(self):
        """Determines area"""
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

    @property
    def position(self):
        """gets position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position"""
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1]:
            raise ValueError('position must be a tuple of 2 positive integers')
        self.__position = position

    def __str__(self):
        """prints square offsetting it by position with symbol #"""
        my_list = []
        if self.__position[1]:
            my_list.append('\n' * self.__position[1])
        for i in range(self.__size):
            if self.__position[0]:
                my_list.append(' ' * self.__position[0])
            my_list.append('#' * self.__size)
            my_list.append('\n')
        if self.__size == 0:
            my_list.append('\n')
        final = ''.join(str(elem) for elem in my_list)
        return(final)
