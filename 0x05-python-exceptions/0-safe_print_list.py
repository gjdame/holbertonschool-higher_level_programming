#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    if my_list:
        for i in range(x):
            try:
                print(my_list[i], end="")
            except IndexError:
                print("")
                return(count)
            else:
                count += 1
    print("")
    return(count)
