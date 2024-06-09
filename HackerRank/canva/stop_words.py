#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stop_words' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING text
#  2. INTEGER k
#

def stopWords(text, k):
    res_list = []
    text = text.strip()
    text = text.lower()
    text_list = text.split()
    freq = {}
    order_list = []
    
    for word in text_list:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
            order_list.append(word)
    
    for word in order_list:
        if freq[word] >= k:
            res_list.append(word)
    
    return res_list
    

if __name__ == '__main__':
    test_case = "the brown fox jumps over the brown dog and runs away to a brown house"
    res =stopWords(test_case,2)
    print(res)