#!/bin/python3

import os


def reverseArray(a):
    for i in range(len(a) // 2):
        a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
