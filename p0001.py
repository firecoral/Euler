#!/usr/local/bin/python

import getopt, sys


def main():
    number = 1
    total = 0
    opt, args = getopt.getopt(sys.argv[1:], ':n:')
    for o, a in opt:
        if o == '-n':
            number = int(a)
        else:
            assert False, "unhandled option"

    total = sum(set(range(3, number, 3) + range(5, number, 5)))
    print "{}: {}".format(number, total)

if __name__ == "__main__":
    main()
