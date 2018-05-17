#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    """append after line if search string is in line
    Args
       filename - file
       search_string - string to search for
       new_string - new string to append after if search is found
    """
    with open(filename, 'r+', encoding='UTF8') as f:
        new_list = []
        for line in f:
            new_list.append(line)
        x = len(new_list)
        for i in range(x):
            if search_string in new_list[i]:
                new_list.insert(i + 1, new_string)
        f.seek(0)
        for i in new_list:
            f.write(i)
