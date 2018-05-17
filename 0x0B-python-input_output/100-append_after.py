#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    """append after line if search string is in line
    Args
       filename - file
       search_string - string to search for
       new_string - new string to append after if search is found
    """
    with open(filename, 'r', encoding='UTF8') as f:
        tmp = f.readlines()

    with open(filename, 'w', encoding='UTF8') as f:
        for line in tmp:
            if search_string in line:
                line = line + new_string
            f.write(line)
