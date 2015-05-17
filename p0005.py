#!/usr/local/bin/python

import getopt, sys

# brute force solution

def main():
    number = 10

    opt, args = getopt.getopt(sys.argv[1:], ':n:')
    for o, a in opt:
        if o == '-n':
            number = int(a)
        else:
            assert False, "unhandled option"

    start = number

    while 1:
        for i in list(reversed(range(1, number + 1))):
            if i == 1:
                print "Success: {}".format(start)
                exit(0)
            if start % i != 0:
                start += number
                break

if __name__ == "__main__":
    main()
