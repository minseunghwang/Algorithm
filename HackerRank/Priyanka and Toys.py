#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    answer = 1
    w.sort()
    min_ = w.pop(0)
    while w:
        if min_ <= w[0] and w[0] <= min_ + 4:
            w.pop(0)
        else:
            min_ = w.pop(0)
            answer += 1
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
