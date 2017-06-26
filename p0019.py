#!/usr/local/bin/python

# #19 counting sundays

import getopt, sys

# start with december since we are interested in the first day of the month
normal = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
leap = [31, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

def main():

    day = -30   # 2 Dec 1899
    count = 0
    for i in range(101):
        if (i % 4 == 0 and i % 100 != 0):
            calendar = leap
            #print "{}: leap".format(i)
        else:
            calendar = normal
            #print "{}: normal".format(i)

        for j in range (len(calendar)):
            day = day + calendar[j]
            if day % 7 == 0 and i != 0:  # Skip 1900
                #print "{}: {}".format(i, j)
                count = count + 1

    print count

if __name__ == "__main__":
    main()
