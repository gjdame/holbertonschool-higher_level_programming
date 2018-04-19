#!/usr/bin/python3


def search_replace(my_list, search, replace):

    new_list = [i if i != search else replace for i in my_list]
    return(new_list)
