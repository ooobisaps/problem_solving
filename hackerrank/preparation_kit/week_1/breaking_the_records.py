#!/bin/python3

import os

def breakingRecords(scores):
    min_score, min_count = scores[0], 0
    max_score, max_count = scores[0], 0
    for score in scores[1:]:
        if score < min_score:
            min_score = score
            min_count += 1
        
        elif score > max_score:
            max_score = score
            max_count += 1
    
    return [max_count, min_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
