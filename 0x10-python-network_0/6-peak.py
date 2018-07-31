#!/usr/bin/python3
'''find peak of unsorted list of ints'''
def find_peak(list_of_integers):
    if not list_of_integers:
        return

    beg = 0
    end = len(list_of_integers) - 1

    mid = (end - beg) // 2

    while (beg != end):
        if list_of_integers[beg] < list_of_integers[mid]:
            beg += 1
            mid = (end - beg) // 2
        elif list_of_integers[end] < list_of_integers[mid]:
            end -= 1
            mid = (end - beg) // 2
        elif list_of_integers[beg] < list_of_integers[end]:
            beg += 1
            mid = (end - beg) // 2
        else:
            end -= 1
            mid = (end - beg) // 2
    return(list_of_integers[end])
