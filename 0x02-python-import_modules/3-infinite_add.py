#!/usr/bin/python3
import sys


def main(argv):

    result = 0

    for i, x in enumerate(argv[1:], 1):
        result += int(x)

    print("{:d}".format(result))

if __name__ == "__main__":
    import sys
    main(sys.argv)
