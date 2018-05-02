#!/usr/bin/python3
import math


class MagicClass:
    """Magic class that does same as given bytecode output"""

    def __init__(self, radius=0):
        """initialize radius"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self, radius):
        """returns area"""
        return (self._MagicClass__radius ** 2 * math.pi)

    def circumference(self, radius):
        """returns circumference"""
        return (2 * math.pi * self._MagicClass__radius)

if __name__ == "__main__":
    import dis
    dis.dis(MagicClass)
