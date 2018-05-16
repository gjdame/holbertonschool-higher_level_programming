#!/usr/bin/python3
import json


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

    def to_json(self):
        """retrieves dictionary representation of instance"""
        return (self.__dict__)
