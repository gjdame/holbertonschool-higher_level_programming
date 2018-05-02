#!/usr/bin/python3


class Node:
    """creates node for singly linked lists"""

    @property
    def data(self):
        """gets data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets data"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """gets link to next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets link to next node"""
        if type(value) is not Node or next_node is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

    def __init__(self, data, next_node=None):
        """initializes node instance
        Args:
            data: data in node
            next_node: next node in list"""
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self.__data = data
        self.__next_node = next_node


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """initializes and prints list"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a node
        Args:
            value: data value of node"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        new_node = Node(value, self.__head)
        self.__head = new_node

    def __str__(self):
        """ creates a list of linked list, sorts, and prints"""
        my_list = []
        if self.__head is None:
            return("")
        runner = self.__head
        while runner is not None:
            my_list.append(runner.data)
            runner = runner.next_node
        my_list.sort()
        final = '\n'.join(str(elem) for elem in my_list)
        return(final)
