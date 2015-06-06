#!/usr/local/bin/python

import getopt, sys, math
from sets import Set


def main():
    number = 4


    opt, args = getopt.getopt(sys.argv[1:], ':n:')
    for o, a in opt:
        if o == '-n':
            number = int(a)
        else:
            assert False, "unhandled option"



    total = 0
    inc = 0
    cur_max = 0
    while True:
        inc += 1
        total += inc
        factors = primes(total)
        #print "{}: {}".format(total, factors)
        count = test(factors)

        if count > cur_max:
            cur_max = count
            print "{}, {}: {}".format(inc, total, count)

        #print "{}: {}".format(total, count)
        if count > number:
            print "{}: {}".format(total, count)
            break

# I guess this is a divisor or tau function
def test(factors):
    primecounts = {}
    for prime in factors:
        if prime in primecounts:
            primecounts[prime] += 1
        else:
            primecounts[prime] = 1
    total = 1
    for primecount in primecounts:
        total *= (primecounts[primecount] + 1)
    return total


def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac



if __name__ == "__main__":
    main()

