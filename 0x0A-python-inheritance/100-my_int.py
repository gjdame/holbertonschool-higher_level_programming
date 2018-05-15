#!/usr/bin/python3


class MyInt(int):
    """class utilizing int class"""

    def __eq__(self, other):
        """initializer for eq"""
        if int.__ne__(self, other):
            return True
        else:
            return False

    def __ne__(self, other):
        """intializer for greater than"""
        if int.__eq__(self, other):
            return True
        else:
            return False
