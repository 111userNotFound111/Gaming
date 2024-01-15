"""
242 Valid Anagram

Given two strings s and t, return true if t is an anagram of s, 
and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

"""
from collections import Counter

# use hash table dictionary 
def detect_anagram(word1,word2):
    word1_list = list(word1)
    word1_freq=Counter(word1_list)
    word2_list = list(word2)
    word2_freq=Counter(word2_list)
    if word1_freq == word2_freq:
        return True
    else:
        return False
    

if __name__ == "__main__":
    word1="anagram"
    word2="nagaram"
    print(detect_anagram(word1,word2))