#!/bin/python3

import os


def diagonalDifference(arr):
    res = 0
    for i in range(len(arr)):
        res += (arr[i][i] - arr[i][len(arr[i]) - i - 1])
    
    return abs(res)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
