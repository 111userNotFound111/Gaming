#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#


# array operations 
# array sorting operation that 
# check if the lis

def twoArrays(k, A, B):
    # two loops 
    A.sort()
    B.sort(reverse=True)

    # check if the largest value of B + smallest value of A satisfy k
    for i in range(len(A)):
        if A[i] + B[i] >= k:
            continue
        else:
            return "NO"
    
    return "YES"
    
    

if __name__ == "__main__":
    A = [0,1]
    B = [0,2]
    k = 1
    print(twoArrays(k,A,B))