"""

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. 

The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

"""
#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    # intialise variables for numbers and ratio for positive, negative and zero
    total = len(arr)
    positive = 0
    negative = 0
    zero = 0
    ratio_positive = 0
    ratio_negative = 0
    ratio_zero = 0
    # special case : empty list
    if total == 0:
        return 0,0,0
    # loop through the array to get amount of positive, negative and zeros
    for num in arr:
        num_int = int(num)
        if num_int > 0:
            positive += 1
        elif num_int < 0:
            negative += 1
        else :
            zero += 1
    # calculate ratio
    ratio_positive = positive / total
    ratio_negative = negative / total
    ratio_zero = zero / total
    # print answers (asked in the question)
    print(ratio_positive)
    print(ratio_negative)
    print(ratio_zero)
    # return answers
    return ratio_positive, ratio_negative, ratio_zero

if __name__ == "__main__":
    testcase = [1,1,0,-1,-1]
    ratio_positive, ratio_negative, ratio_zero = plusMinus(testcase)
    print(ratio_positive)
    print(ratio_negative)
    print(ratio_zero)