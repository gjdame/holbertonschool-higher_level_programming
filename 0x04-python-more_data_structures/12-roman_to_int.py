#!/usr/bin/python3


def roman_to_int(roman_string):

    if roman_string and isinstance(roman_string, str):
        list_n = []
        total = 0
        nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50,
                'X': 10, 'V': 5, 'I': 1}
        for i in roman_string:
            if i in nums.keys():
                list_n.append(nums[i])

        len_l = len(list_n)
        if len_l == 1:
            total = list_n[0]
            return total

        for i in range(len_l - 1):
            if list_n[i] < list_n[i + 1]:
                total -= list_n[i]
            else:
                total += list_n[i]
        total += list_n[i + 1]
        return total
