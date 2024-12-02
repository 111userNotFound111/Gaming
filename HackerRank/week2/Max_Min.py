"""
You will be given a list of integers, arr , and a single integer k. You must create an array of length k from elements of arr' such that its unfairness is minimized. 
Call that array . Unfairness of an array is calculated as
                max(arr') - min(arr')
Where:
- max denotes the largest integer in arr'
- min denotes the smallest integer in  arr'

Example

arr = [1,4,7,2]
k = 2

Pick any two elements, say arr' = [4,7].

Testing for all pairs, the solution  [1,2] provides the minimum unfairness.

Note: Integers in arr may not be unique.

Function Description

Complete the maxMin function in the editor below.
maxMin has the following parameter(s):

int k: the number of elements to select
int arr[n]:: an array of integers
Returns

int: the minimum possible unfairness

"""

# Aim : find the minimal difference between two number with gap k 
# loop through the array: find minimal differences
def maxMin(k, arr):
    minimal = -1
    arr_sorted = sorted(arr)
    k = int(k)
    index = 0
    gap = k - 1
    
    while index <= len(arr_sorted)-k:
        print(index)
        
        next_val = index + gap
        min_curr = arr_sorted[next_val] - arr_sorted[index]
        
        if minimal == -1:
            minimal = min_curr
        elif min_curr < minimal:
            minimal = min_curr
        
        index += 1
        
    return minimal


if __name__ == "__main__":
    k = 2
    arr = [1,4,7,2]
    print(maxMin(k, arr))