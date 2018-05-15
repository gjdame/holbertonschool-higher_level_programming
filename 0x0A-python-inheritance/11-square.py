#!/usr/bin/python3


class BaseGeometry:
    """base geometry class"""

    def area(self):
        """unimplemented area function"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer validator
        Args
           name
           value
        must be int greater than 0"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """initializer
        Args
           width
           height
        """
        if not super().integer_validator('width', width):
            self.__width = width
        if not super().integer_validator('height', height):
            self.__height = height

    def area(self):
        """area of rectangle"""
        return(self.__height * self.__width)

    def __str__(self):
        """returns string of rectangle format"""
        return('[Rectangle] {}/{}'.format(self.__width, self.__height))


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """initalizer
        Args
           size: size of side of square
        """
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """returns dimension of square"""
        return('[Square] {}/{}'.format(self.__size, self.__size))
