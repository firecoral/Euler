#!/usr/local/bin/python

import getopt, sys


def main():
    n = 2

    opt, args = getopt.getopt(sys.argv[1:], ':n:')
    for o, a in opt:
        if o == '-n':
            n = int(a)
        else:
            assert False, "unhandled option"


    print sum(map(int, str(2**1000)))
    exit(0)




if __name__ == "__main__":
    main()

