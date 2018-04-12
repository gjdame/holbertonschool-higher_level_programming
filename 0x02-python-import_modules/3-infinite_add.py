#!/usr/bin/python3
import sys


def main(argv):

    result = 0

    if len(argv) - 1 == 0:
      print("{:d}".format(result))
    else:
        for i, x in enumerate(argv[1:], 1):
            result += int(x)

    print("{:d}".format(result))

if __name__ == "__main__":
    import sys
    main(sys.argv)
