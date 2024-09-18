#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#


# k sum question 
# find number of subarray with length m and sum d

def birthday(s, d, m):
    counter = 0
    gap = m-1
    for i in range(len(s) - gap):
        if sum(s[i:i+m]) == d:
            counter += 1
    
    return counter

if __name__ == '__main__':
    s= [2,2,1,3,2]
    d=4
    m=2
    print(birthday(s,d,m))