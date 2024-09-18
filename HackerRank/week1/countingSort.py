#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    
    max_num = max(arr)
    
    freq_list = [0] * (max_num + 1)

    for num in arr:
        freq_list[num] += 1
    
    return freq_list


if __name__ == '__main__':
    test_case = [1,2,3,10,10,10]
    print(countingSort(test_case))
