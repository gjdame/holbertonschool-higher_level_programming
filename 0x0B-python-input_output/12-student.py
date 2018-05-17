#!/usr/bin/python3


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """initalizer
        Args
           first_name
           last_name
           age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation of instance"""
        if attrs is None:
            return (self.__dict__)
        if not isinstance(attrs, list):
            return (self.__dict__)
        if not (isinstance(attrs[elem], str) for elem in attrs):
            return (self.__dict__)
        return ({key: value for key, value in self.__dict__.items()
                 if key in attrs})
