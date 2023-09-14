"""
49 Group Anagrams

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

"""

from collections import defaultdict

def groupAnagrams(strs):
    # the hash mapping data struct is 
    # {(character num in this anagram):[list of anagrams]}
    # for example (t:1,e:1,a:1)
    anagram_dict=defaultdict(list)
    output_list=[]
    for word in strs:
        # create a list for 
        character_list = [0]*26
        for char in word:
            char_index=ord(char)-ord("a")
            character_list[char_index] += 1
        
        # convert list into tuple use as key in dictionary
        # tuple is a hashable struct 
        anagram_dict[tuple(character_list)].append(word)

    for group in anagram_dict.values():
        #print(group)
        group=sorted(group)
        output_list.append(group)
    
    output_list=sorted(output_list, key=len)
    return output_list


if __name__ == "__main__":
    strs=["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))