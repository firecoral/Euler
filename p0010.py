#!/usr/local/bin/python

import getopt, sys


def main():
    number = 10
    total = 0

    opt, args = getopt.getopt(sys.argv[1:], ':n:')
    for o, a in opt:
        if o == '-n':
            number = int(a)
        else:
            assert False, "unhandled option"

    for i in range(number):
        if is_prime(i):
            total += i

    print total

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True    

if __name__ == "__main__":
    main()
