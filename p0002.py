#!/usr/local/bin/python

import getopt, sys


def main():
    number = 1
    list = [1, 2]
    total = 0

    opt, args = getopt.getopt(sys.argv[1:], ':n:')
    for o, a in opt:
        if o == '-n':
            number = int(a)
        else:
            assert False, "unhandled option"

    while 1:
        new = list[-1] + list[-2]
        if new < number:
            list.append(new)
        else:
            break

    print list;

    for i in range(0, len(list)):
        if list[i] % 2 == 0:
            total += list[i]
        #print "{}: {}".format(list[i], total)

    print total

if __name__ == "__main__":
    main()
