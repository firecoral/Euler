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


    path = ""
    print node(path, n, 0, 0)
    exit(0)

def node(path, n, x, y):
    path += " ({},{})".format(x, y)
    count = 0
    if x == n and y == n:
        print "{}: {}".format(path, count)
        return 1
    if x < n:
        count += node(path, n, x+1, y)
    if y < n:
        count += node(path, n, x, y+1)
    #print "{}: {}".format(path, count)
    if y == 0:
        print "{} - {}".format(x, count);
    return count




if __name__ == "__main__":
    main()

