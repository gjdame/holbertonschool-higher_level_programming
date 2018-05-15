#!/usr/bin/python3


class BaseGeometry:

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        if not super().integer_validator('width', width):
            self.__width = width
        if not super().integer_validator('height', height):
            self.__height = height

    def area(self):
        return(self.__height * self.__width)

    def __str__(self):
        return('[Rectangle] {}/{}'.format(self.__width, self.__height))

class Square(Rectangle):

    def __init__(self, size):
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        return('[Square] {}/{}'.format(self.__size, self.__size))
