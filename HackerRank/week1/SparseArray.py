#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

# matching string function 
def matchingStrings(strings, queries):
    res = []
    freq_dict = {}
    # part 1 storage 
    # store freq of each word in dict
    for word in strings:
        word = word.strip()
        freq_dict[word] = 1 + freq_dict.get(word,0)


    # part 2 search 
    # from queries, get all the freq and store in res
    for query in queries:
        query = query.strip()
        freq = freq_dict.get(query,0)
        res.append(freq)

    return res

if __name__ == '__main__':
    strings = ['ab',' ab', ' abc']
    queries = [' ab', 'abc', 'bc']
    print(matchingStrings(strings, queries))
