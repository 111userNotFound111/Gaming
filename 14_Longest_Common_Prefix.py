"""

14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""

def longestCommonPrefix(strs) -> str:
    # longest prefix
    prefix=""
    prefix_length=1
    
    for i in range(len(strs[0])):
        
        prefix = strs[0][:prefix_length]
        
        for j in range(len(strs)):
            if prefix == strs[j][:prefix_length]:
                continue
            else:
                return prefix[:prefix_length-1]
    
        prefix_length += 1
    
    return prefix

def longestCommonPrefix_1(strs) -> str:
    
    # the common prefix must be in both first and last str in a list sorted in alphabetical order 
    strs_sorted = sorted(strs)
    first = strs_sorted[0]
    last = strs_sorted[-1]
    
    output=""
    
    shortest = min(len(first), len(last))
    
    for i in range (shortest):
        if first[i] != last[i]:
            return  output
    
        output +=first[i]
    
    return output
if __name__ == "__main__":
    strs = ["dog","acecar","car"]
    print(longestCommonPrefix_1(strs))