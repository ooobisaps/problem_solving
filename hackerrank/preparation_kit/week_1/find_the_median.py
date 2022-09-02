#!/bin/python3

import os


def findMedian(arr, n):
    sorted_arr = sorted(arr)
    return sorted_arr[n // 2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
