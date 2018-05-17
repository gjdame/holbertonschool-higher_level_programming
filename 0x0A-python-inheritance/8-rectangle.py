#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
