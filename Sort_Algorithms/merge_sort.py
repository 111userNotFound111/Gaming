"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""

# for O(nlogn) we use merge sort
# divide and conquer technique 

def sortArray(nums):
    # part 1 : dividing array into many array containing single element recursively
    if len(nums) > 1:
        mid = len(nums) // 2
        L = nums[:mid]
        R = nums[mid:]
    
        sortArray(L)
        sortArray(R)
        
    # part 2 : sort and merge
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
        # check for unequal length L and R
        while k < len(nums):
            if i < len(L):
                nums[k] = L[i]
                k += 1
                i += 1
            else:
                nums[k] = R[j]
                k += 1
                j += 1
    return nums

if __name__ == "__main__":
    nums = [5,1,1,2,0,0]
    print(sortArray(nums))