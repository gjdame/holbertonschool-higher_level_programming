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
        Must be an int greater than 0"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """initializer
        Args
           width
           height
        """
        if super().integer_validator('width', width):
            self.__width = width
        if super().integer_validator('height', height):
            self.__height = height
