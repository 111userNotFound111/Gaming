"""

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Sample Input
[1 2 3 4 5]

Sample Output
10 14

"""
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    array_ordered = sorted(arr)
    array_min = array_ordered[:4]
    array_max = array_ordered[1:5]


    sum_min = sum(array_min)
    sum_max = sum(array_max)

    print(f"{sum_min} {sum_max}")
    return

if __name__ == "__main__":
    testcase = [7, 69, 2, 221, 8974]
    res = miniMaxSum(testcase)
    print(res)