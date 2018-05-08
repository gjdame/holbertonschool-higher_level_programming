#!/usr/bin/python3


class Rectangle:
    """class Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializer
        Args
           width
           height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """computers area"""
        res = self.width * self.height
        return(res)

    def perimeter(self):
        """computers perimeter"""
        if self.width == 0 or self.height == 0:
            res = 0
            return(res)
        res = (self.width * 2) + (self.height * 2)
        return(res)

    def __str__(self):
        """prints rectangle"""
        if self.height == 0 or self.width == 0:
            return ''
        hashes = "{}".format(self.print_symbol) * self.width
        return '\n'.join(hashes for i in range(self.height))

    def __repr__(self):
        """prints rectangle"""
        eval('Rectangle(self.width, self.height)')
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """compares two Rectangles
        Args
           rect_1
           rect_2
        Returns bigger rectangle or rect_1 if same
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return(rect_1)
        else:
            return(rect_2)

    @classmethod
    def print_symbol(cls, symbol):
        Rectangle.print_symbol = symbol

    @property
    def width(self):
        """gets width"""
        return self.__width

    @property
    def height(self):
        """gets height"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets width
        Args:
        value: width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets height
        Args:
        value: height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
