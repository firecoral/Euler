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

    ones = []
    ones.append({ 'digit': '', 'total' : 0 })
    ones.append({ 'digit': 'one', 'total' : 3 })
    ones.append({ 'digit': 'two', 'total' : 3 })
    ones.append({ 'digit': 'three', 'total' : 5 })
    ones.append({ 'digit': 'four', 'total' : 4 })
    ones.append({ 'digit': 'five', 'total' : 4 })
    ones.append({ 'digit': 'six', 'total' : 3 })
    ones.append({ 'digit': 'seven', 'total' : 5 })
    ones.append({ 'digit': 'eight', 'total' : 5 })
    ones.append({ 'digit': 'nine', 'total' : 4 })
    ones.append({ 'digit': 'ten', 'total' : 3 })
    ones.append({ 'digit': 'eleven', 'total' : 6 })
    ones.append({ 'digit': 'twelve', 'total' : 6 })
    ones.append({ 'digit': 'thirteen', 'total' : 8 })
    ones.append({ 'digit': 'fourteen', 'total' : 8 })
    ones.append({ 'digit': 'fifteen', 'total' : 7 })
    ones.append({ 'digit': 'sixteen', 'total' : 7 })
    ones.append({ 'digit': 'seventeen', 'total' : 9 })
    ones.append({ 'digit': 'eighteen', 'total' : 8 })
    ones.append({ 'digit': 'nineteen', 'total' : 8 })

    tens = []
    tens.append({ 'digit': '', 'total' : 0 })
    tens.append({ 'digit': 'ten', 'total' : 3 })
    tens.append({ 'digit': 'twenty', 'total' : 6 })
    tens.append({ 'digit': 'thirty', 'total' : 6 })
    tens.append({ 'digit': 'forty', 'total' : 5 })
    tens.append({ 'digit': 'fifty', 'total' : 5 })
    tens.append({ 'digit': 'sixty', 'total' : 5 })
    tens.append({ 'digit': 'seventy', 'total' : 7 })
    tens.append({ 'digit': 'eighty', 'total' : 6 })
    tens.append({ 'digit': 'ninety', 'total' : 6 })

    hundreds = []
    hundreds.append({ 'digit': '', 'total' : 0 })
    hundreds.append({ 'digit': 'one hundred', 'total' : 10 })
    hundreds.append({ 'digit': 'two hundred', 'total' : 10 })
    hundreds.append({ 'digit': 'three hundred', 'total' : 12 })
    hundreds.append({ 'digit': 'four hundred', 'total' : 11 })
    hundreds.append({ 'digit': 'five hundred', 'total' : 11 })
    hundreds.append({ 'digit': 'six hundred', 'total' : 10 })
    hundreds.append({ 'digit': 'seven hundred', 'total' : 12 })
    hundreds.append({ 'digit': 'eight hundred', 'total' : 12 })
    hundreds.append({ 'digit': 'nine hundred', 'total' : 11 })


    total = 0
    total2 = 0
    for i in range (1, 1001):
        sum2 = 0
        str1 = ''
        if i == 1000:
            str1 += 'one thousand'
            sum2 += 11
        else:
            if i > 99:
                hundred = i / 100
                str1 += hundreds[hundred]['digit']
                sum2 += hundreds[hundred]['total']
                if i % 100 != 0:
                    str1 += ' and '
                    sum2 += 3
            tenone = i % 100
            if tenone < 20:
                str1 += ones[tenone]['digit']
                sum2 += ones[tenone]['total']
            else:
                ten = tenone / 10
                str1 += tens[ten]['digit']
                sum2 += tens[ten]['total']
                one = tenone % 10
                if ten != 0 and one != 0:
                    str1 += '-'
                str1 += ones[one]['digit']
                sum2 += ones[one]['total']

        tmpstr = str1
        tmpstr2 = tmpstr.replace(' ', '');
        tmpstr3 = tmpstr2.replace('-', '');
        total += len(tmpstr3)
        total2 += sum2
        print "{}({}, {}): {} : {}".format(i, len(tmpstr3), sum2, str1, tmpstr3)

    print total
    print total2
    exit(0)




if __name__ == "__main__":
    main()

