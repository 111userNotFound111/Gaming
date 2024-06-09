#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isPossible' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#  4. INTEGER d
#
def travelfunction (a, b, c, d):
    print("current ", a , b)
    
    # stop case
    if (a,b) == (c,d):
        return True
    if a > c or b > d:
        return False
    # recursive case
    new_a = a + b
    if travelfunction(new_a, b , c, d ):
        return True
    new_b = a + b
    if travelfunction(a, new_b, c, d):
        return True

    return False

def isPossible(a, b, c, d):
    print("dest", c, d)
    res = travelfunction(a,b,c,d)
    return res
if __name__ == '__main__':
    a = 1
    b = 1
    c = 1000
    d = 1000
    
    res = isPossible(a,b,c,d)
    print(res)