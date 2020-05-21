#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    answer = 0
    d1 = defaultdict(int)
    d2 = defaultdict(int)

    for i in a:
        d1[i] += 1
    for i in b:
        d2[i] += 1

    for i in b:
        if (i in d1) and (d1[i] != 0):
            d1[i] -= 1
        else:
            answer += 1

    for i in a:
        if (i in d2) and (d2[i] != 0):
            d2[i] -= 1
        else:
            answer += 1


    return answer


if __name__ == '__main__':
    a = input()
    b = input()
    print(makeAnagram(a, b))

