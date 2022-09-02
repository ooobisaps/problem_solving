#!/bin/python3

def plusMinus(arr):
    positive_count, negative_count, zero_count = 0, 0, 0
    for item in arr:
        if item > 0:
            positive_count += 1
        elif item < 0:
            negative_count += 1
        else:
            zero_count += 1

    print(round(positive_count / len(arr), 6))
    print(round(negative_count / len(arr), 6))
    print(round(zero_count / len(arr), 6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
