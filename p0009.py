#!/usr/local/bin/python

import getopt, sys
from sets import Set


def main():
    number = 12

    opt, args = getopt.getopt(sys.argv[1:], ':n:')
    for o, a in opt:
        if o == '-n':
            number = int(a)
        else:
            assert False, "unhandled option"

    squares = []
    for i in range(0, number + 1):
        squares.append(i * i)
    squares_set = Set(squares)

    for a in range(0, number):
        for b in range(0, number):
            c = number - (a + b);
            if c <= 0:
                continue;
            val = squares[a] + squares[b]
            #print "{}, {}, {} : {}, {}, {}".format(a, b, c, squares[a], squares[b], squares[c])
            if val == squares[c]:
                print "{}, {}, {}".format(a, b, c)


if __name__ == "__main__":
    main()
