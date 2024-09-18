#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


# aim of this question is for beginner matrix calculations 

def diagonalDifference(arr):
    res = 0
    left_diagonal = 0
    right_diagonal = 0
    i = 0
    
    # if empty arr 
    if len(arr) == 0:
        return 0
    
    # for left diagonal
    while i < len(arr):
        left_diagonal += arr[i][i]
        i += 1
    
    # for right diagonal
    for j in range(len(arr)):
        # the i value is initially out of bound
        i -= 1
        right_diagonal += arr[j][i]
        
    res = abs(left_diagonal - right_diagonal)
    return res

if __name__ == '__main__':
    test_case = [[1,2,3],[4,5,6],[9,8,9]]
    print(diagonalDifference(test_case))