#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# aim : 
# 1. efficient data structure 
# 2. string manipulations
def pangrams(s):
    counter = 26
    alphabet_list = [0] * 26
    s = s.strip()
    s = s.replace(' ','')
    s = s.lower()
    print(s)
    for char in s:
        ascii_code = ord(char)
        print(ascii_code, char)
        alphabet_pos = int(ascii_code) - 97
        if alphabet_list[alphabet_pos] == 0:
            alphabet_list[alphabet_pos] += 1
            counter -= 1
        else:
            continue

    if counter > 0:
        return print("not pangram")

    return print("pangram")

if __name__ == '__main__':
    testcase = 'The quick brown fox jumps over the lazay dog'
    pangrams(testcase)