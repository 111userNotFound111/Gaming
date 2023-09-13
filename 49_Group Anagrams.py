"""
49 Group Anagrams

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

from collections import Counter

def group_anagrams(strs):
    hash_set = set()
    output_list=[]
    # get dic of one of the 
    for index in range(0,len(strs)):
        if strs[index] in hash_set:
            continue
        group_list=[strs[index]]
        word_dict=Counter(strs[index])
        
        if index + 1 <= len(strs):
            for compare_index in range (index+1, len(strs)):
                
                compare_word_dict=Counter(strs[compare_index])
                if word_dict==compare_word_dict:
                    group_list.append(strs[compare_index])
                    hash_set.add(strs[compare_index])
            group_list=sorted(group_list)
            output_list.append(group_list)
    output_list=sorted(output_list, key=len)
    return output_list 

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(group_anagrams(strs))