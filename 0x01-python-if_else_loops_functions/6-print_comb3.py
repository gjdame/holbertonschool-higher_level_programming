#!/usr/bin/python3
for i in range(0, 90):
    tens = i / 10
    mod = i % 10

    if mod > tens:
        if i != 89:
            print("{}".format('%02d' % i), end=", ")
        else:
            print("{}".format('%02d' % i))
