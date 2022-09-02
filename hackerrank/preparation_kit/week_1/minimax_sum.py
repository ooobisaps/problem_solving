#!/bin/python3

def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    sorted_array_sum = sum(sorted_arr)
    print(f"{sorted_array_sum - sorted_arr[-1]} {sorted_array_sum - sorted_arr[0]}")


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
