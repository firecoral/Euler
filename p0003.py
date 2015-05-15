#!/usr/local/bin/python

import getopt, sys


def main():
    number = 600851475143

    opt, args = getopt.getopt(sys.argv[1:], ':n:')
    for o, a in opt:
        if o == '-n':
            number = int(a)
        else:
            assert False, "unhandled option"

    test_prime(2, number)


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

def test_prime(prime, number):
    print "test_prime({}, {})".format(prime, number)
    sys.stdout.flush()
    i = prime
    while i <= number:
        if is_prime(i):
            if number % i == 0:
                print i
                sys.stdout.flush()
                test_prime(i, number / i)
                return;
        i += 1


if __name__ == "__main__":
    main()
