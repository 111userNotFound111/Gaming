#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # 1. create the cipher based on int k 
    # 2. the question uses left shift
    # 3. loop through and encode the string s
    # 4. return output 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cutting_point = k % 26
    encrypted_code = alphabet[cutting_point:] + alphabet[:cutting_point]
    # for faster encrypt decrypt speed, use hash
    encrypted_dict = {} # key = alphabet value = encoded

    for i in range(26):
        encrypted_dict[alphabet[i]] = encrypted_code[i]
    res = str()

    for char in s:
        upperflag = False
        # check for uppercase letter
        if char.isupper() == True:
            char = char.lower()
            upperflag = True

        if char in encrypted_dict.keys():
            char_encoded = encrypted_dict[char]
            if upperflag == False:
                res += char_encoded
            else:
                res += char_encoded.upper()
        else:
            res += char
    
    return res

if __name__ == "__main__":
    s = "middle-Outz"
    n = 2
    caesarCipher(s,n)