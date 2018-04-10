#!/usr/bin/env python3
def uppercase(str):
    new_str = ""
    for i in str:
        char = ord(i)
        if 96 < char < 123:
            char = char - 32
        new_str += i
    print (new_str)
