#!/usr/local/bin/python

import getopt, sys


def main():
    number = 13


    opt, args = getopt.getopt(sys.argv[1:], ':n:')
    for o, a in opt:
        if o == '-n':
            number = int(a)
        else:
            assert False, "unhandled option"

    cur_max = 0
    for i in range(1, 1000000):
        count = func(i)
        if count > cur_max:
            cur_max = count
            print "{}: {}".format(i, count)

def func(value):
    if value == 1:
        return 1;
    if value % 2 == 0:
        return 1 + func(value / 2)
    else:
        return 1 + func(value * 3 + 1)


if __name__ == "__main__":
    main()

