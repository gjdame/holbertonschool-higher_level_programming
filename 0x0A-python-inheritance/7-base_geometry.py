#!/usr/bin/python3


class BaseGeometry:
    """base geometry class"""

    def area(self):
        """unimplemented area function"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer validation
        Args
           name: name of value
           value: value

        Must be an int greater than 0
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
