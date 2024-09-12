"""
Given an array of  distinct integers, transform the array into a zig zag sequence by permuting the array elements. A sequence will be called a zig zag sequence if the first  elements in the sequence are in increasing order and the last  elements are in decreasing order, where . You need to find the lexicographically smallest zig zag sequence of the given array.

Example.


Now if we permute the array as , the result is a zig zag sequence.

Debug the given function findZigZagSequence to return the appropriate zig zag sequence for the given input array.

Note: You can modify at most three lines in the given code. You cannot add or remove lines of code.

To restore the original code, click on the icon to the right of the language selector.

"""


'''
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return
'''

# the question ask to debug this function 
# can only change three lines of code 

def findZigZagSequence(a, n):
    a.sort()  
    mid = n //2  # frist line 
    a[mid], a[n-1] = a[n-1], a[mid] 

    st = mid + 1 
    ed = n - 2 # second line
    while(st <= ed):
        print(st, ed)
        a[st], a[ed] = a[ed], a[st]
        print(a)
        st = st + 1
        ed = ed - 1 # third line 

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

if __name__ == "__main__": 
    input_array = [1, 2, 3, 4, 5, 6, 7]
    findZigZagSequence(input_array, len(input_array))