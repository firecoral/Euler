#!/usr/local/bin/python

import getopt, sys


def main():
    number = 1
    max_pal = 0

    opt, args = getopt.getopt(sys.argv[1:], ':n:')
    for o, a in opt:
        if o == '-n':
            number = int(a)
        else:
            assert False, "unhandled option"

    l = list(reversed(range(number)))
    for i in l:
        for j in l:
            val = i * j
            if val < max_pal:
                continue
            if ispalindrome(val):
                if max_pal < val:
                    max_pal = val

    print max_pal

def ispalindrome(value):
    l_val = list(str(value))
    checks = len(l_val) / 2
    for i in range(checks):
        #print "{}: {} != {}".format(value, l_val[i], l_val[-(i+1)])
        if l_val[i] != l_val[-(i+1)]:
            return False
    return True

if __name__ == "__main__":
    main()
