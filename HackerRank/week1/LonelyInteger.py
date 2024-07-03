#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    a_sort = sorted(a)
    last_index = len(a_sort) - 1
    # even number jump pointer start from 1
    pointer = 1

    while pointer < last_index:
        print(a_sort[pointer-1],a_sort[pointer])

        if a_sort[pointer-1] != a_sort[pointer]:
            return a_sort[pointer-1]
        else:
            pointer += 2
        
    return a_sort[pointer-1]




if __name__ == "__main__":
    test_array = [1,2,3,4,3,2,1]
    print(lonelyinteger(test_array))