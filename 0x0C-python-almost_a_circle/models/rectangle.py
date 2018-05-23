#!/usr/bin/python3

'''
Defines the class Rectangle
'''
from models.base import Base
import sys


class Rectangle(Base):
    """rectangle class almost a circle project"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """intializer for Rectangle class
        Args
           width
           height
           x
           y
           id - from Base class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets width
        Args
           value
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format('width'))
        if value <= 0:
            raise ValueError('{} must be > 0'.format('width'))
        self.__width = value

    @property
    def height(self):
        """gets height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets height
        Args
           value
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format('height'))
        if value <= 0:
            raise ValueError('{} must be > 0'.format('height'))
        self.__height = value

    @property
    def x(self):
        """gets x"""
        return(self.__x)

    @x.setter
    def x(self, value):
        """sets x
        Args
           x
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format('x'))
        if value < 0:
            raise ValueError('{} must be >= 0'.format('x'))
        self.__x = value

    @property
    def y(self):
        """gets y"""
        return(self.__y)

    @y.setter
    def y(self, value):
        """sets y
        Args
           y
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format('y'))
        if value < 0:
            raise ValueError('{} must be >= 0'.format('y'))
        self.__y = value

    def area(self):
        """returns area of rectangle"""
        return(self.height * self.width)

    def display(self):
        """displays rectangle"""
        print('\n' * self.y, end="")
        for i in range(self.height):
            print(' ' * self.x, end="")
            print('#' * self.width)

    def __str__(self):
        """returns string of info about rectangle"""
        return('[Rectangle] ({}) {}/{} - {}/{}'
               .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """assigns arguments to each attribute"""
        if args:
            keys = ['id', 'width', 'height', 'x', 'y']
            for k, v in zip(keys, args):
                setattr(self, k, v)
        else:
            keys = ['id', 'width', 'height', 'x', 'y']
            if kwargs is not None:
                for k, v in kwargs.items():
                    if k in keys:
                        setattr(self, k, v)

    def to_dictionary(self):
        """dictiobnary representation of rectangle"""
        my_dic = {}
        keys = ['id', 'width', 'height', 'x', 'y']

        for k in keys:
            my_dic[k] = getattr(self, k)
        return(my_dic)
