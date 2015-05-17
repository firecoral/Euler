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

    numbers = range(1, number + 1)
    
    total = 0
    for i in numbers:
        total += i ** 2

    square_of_sum = sum(numbers) ** 2

    print "{} - {} = {}".format(square_of_sum, total, square_of_sum - total)

if __name__ == "__main__":
    main()
