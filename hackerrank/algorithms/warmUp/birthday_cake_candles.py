#!/bin/python3

import os


def birthdayCakeCandles(candles):
    candles_stat, candles_max = {}, -1
    for candle in candles:
        if candle > candles_max:
            candles_max = candle
        
        candles_stat[candle] = candles_stat.get(candle, 0) + 1
    
    return candles_stat.get(candles_max)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
