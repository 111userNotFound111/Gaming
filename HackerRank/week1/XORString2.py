"""
In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.

To know more about XOR Click Here

Debug the given function strings_xor to find the XOR of the two given strings appropriately.

Note: You can modify at most three lines in the given code and you cannot add or remove lines to the code.

To restore the original code, click on the icon to the right of the language selector.

Input Format

The input consists of two lines. The first line of the input contains the first string, , and the second line contains the second string t.


"""

# can only debug max 3 lines 
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res

s = [1,0,1,0,1]
t = [0,0,1,0,1]
print(strings_xor(s, t))