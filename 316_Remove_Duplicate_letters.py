"""

316. Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is 
the smallest in lexicographical order among all possible results.

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""

def removeDuplicateLetters(s):
    combination_list = []
    scanned_set = set()
    combination_str = ""
    
    for i in range(len(s)-1):
        scanned_set.add(s[i])
        combination_str += s[i]
        for j in range(i+1, len(s)-2):
            if s[j] not in scanned_set:
                scanned_set.add(s[j])
                combination_str += s[j]
                print(scanned_set)
                print(combination_str)
    
        combination_list.append(combination_str)
        scanned_set=set()
        combination_str=""
    
    print(combination_list)
    
if __name__ == "__main__":
    s = "bcabc"
    removeDuplicateLetters(s)