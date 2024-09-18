#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#



# the aim of this question is :
# 1. base conversions using % (mod)
# 2. padding to add units until its base32
# 3. data type conversion (str to int & int to str)


def convert_base2(n):
    res = str()
    if n == 0:
        return 1
    while n > 0:
        remainder = n % 2
        # convert 1 to 0 and vice versa 
        if remainder == 1:
            remainder = 0
        else:
            remainder = 1
            
        res = str(remainder) + res
        n = n // 2
    return res

def add_padding(base2_str):
    # add 1 padding in front to make it base32
    print(type(base2_str))
    gap = 32 - len(base2_str)
    padding = "1" * gap
    res = padding + base2_str
    return res

def convert_base10(n):
    res = int(n,2)
    return res

def flippingBits(n):
    # convert n to int type 
    n = int(n)
    # converts base10 to base2
    base2_int = convert_base2(n)
    # add padding to make it base32
    base32_int = add_padding(base2_int)
    # convert base2 to base10
    base10_int = convert_base10(base32_int)
    return base10_int
    
if __name__ == "__main__":
    test_case = 9
    print(flippingBits(test_case))