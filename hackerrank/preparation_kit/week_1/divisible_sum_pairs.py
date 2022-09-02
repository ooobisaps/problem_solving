#!/bin/python3

import os


def divisibleSumPairs(k, ar):
    pairs_count, pairs = 0, {}
    for item in ar:
        mod = item % k
        diff = 0 if mod == 0 else k - mod

        if diff in pairs:
            pairs_count += pairs.get(diff)

        if mod in pairs:
            pairs[mod] += 1
        else:
            pairs[mod] = 1

    return pairs_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
