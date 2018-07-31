#!/usr/bin/python3
'''find peak of unsorted list of ints'''


def find_peak(list_of_integers):
    if not list_of_integers:
        return

    beg = 0
    end = len(list_of_integers) - 1
    return(peak(list_of_integers, 0, end))


def peak(list_int, low, high):

    if low == high:
        return(list_int[high])
    mid = (high + low) // 2
    if list_int[mid] > list_int[mid + 1]:
        return(peak(list_int, low, mid))
    return(peak(list_int, mid + 1, high))
