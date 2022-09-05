#!/bin/python3

import os


def lonelyinteger(arr):
    res = arr[0]
    for item in arr[1:]:
        res ^= item
    return item

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
