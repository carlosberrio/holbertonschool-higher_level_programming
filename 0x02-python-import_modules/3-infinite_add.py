#!/usr/bin/python3
import sys

if __name__ == '__main__':
    rem = sys.argv
    o_rem = len(rem)
    sum = 0

    if o_rem > 1:
        for i in range(1, o_rem):
            sum += int(rem[i])

    print(sum)