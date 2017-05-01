#!/usr/local/bin/python

import getopt, sys

# Not sure there is much you can do here except brute force.
# Could map/reduce to simplify loops

def main():
    opt, args = getopt.getopt(sys.argv[1:], ':n:')
    for o, a in opt:
        if o == '-n':
            number = int(a)
        else:
            assert False, "unhandled option"

    total = 1
    for i in range(1, number + 1):
        total = total * i

    print total
    digit_total = 0
    while total > 0:
        digit_total = digit_total + total % 10;
        total = total / 10

    print digit_total


if __name__ == "__main__":
    main()
