#!/usr/bin/python3
'''find peak of unsorted list of ints'''
def find_peak(list_of_integers):
    if not list_of_integers:
        return

    beg = 0
    end = len(list_of_integers) - 1

    while (beg < end):
        if list_of_integers[beg] > list_of_integers[end]:
            peak = list_of_integers[beg]
            end -= 1
        else:
            peak = list_of_integers[end]
            beg += 1
    return(peak)
