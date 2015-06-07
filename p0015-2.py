#!/usr/local/bin/python

import getopt, sys


def main():
    n = 7

    opt, args = getopt.getopt(sys.argv[1:], ':n:')
    for o, a in opt:
        if o == '-n':
            n = int(a)
        else:
            assert False, "unhandled option"


    matrix = [[0 for col in range(n)] for row in range(n)]
    matrix[0][0] = 1;
    #matrix[0][1] = 1;
    for i in range(n):
        matrix[i][0] = 1;
        for j in range(1, n):
            if j > i:
                #sums[i] = sum(matrix[i])
                matrix[i][j] = sum(matrix[i])
                #print "{}: sum: {} matrix: {}".format(i, sums[i], matrix[i])
                break
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]


    for i in range(n):
        print matrix[i]

    for i in range(n):
        print "{}: {}".format(matrix[i][1] - 1, matrix[i][i])
    exit(0)




if __name__ == "__main__":
    main()

