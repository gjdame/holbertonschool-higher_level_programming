#!/usr/bin/python3


class MyList(list):

    def __init__(self):
        pass

    def print_sorted(self):
        res = list.copy(self)
        list.sort(res)
        print(res)
