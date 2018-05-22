#!/usr/bin/python3

'''
Defines the class Base
'''
import json


class Base:
    """base class for almost a circle project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializer
        Args
           id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string of dictionaries"""
        if not list_dictionaries:
            return('[]')
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string represntation to a file
        Args
           cls - class
           list_objs - list objects
        """

        filename = '{}.json'.format(cls.__name__)

        my_list = []
        if list_objs:
            for x in list_objs:
                my_list.append(x.to_dictionary())
        my_list = cls.to_json_string(my_list)
        with open(filename, 'w') as f:
            f.write(my_list)

    @staticmethod
    def from_json_string(json_string):
        """returns a list of the json string representation
        Args
           json_string - represents a list of dictionaries
        """
        return(json.loads(json_string or []))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set
        Args
            cls - class
            **dictionary - double pointer to a dictionary
        """
        tmp = cls(1, 1)
        tmp.update(**dictionary)
        return(tmp)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances of cls
        Args
           cls - class
        """
        my_list = []
        filename = '{}.json'.format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                    my_list = cls.from_json_string(f.read())
            return([cls.create(**x) for x in my_list])
        except FileNotFoundError:
            return([])
