"""

31. Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.


Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

"""


# The aim is to find the next permutation (lexicographically greater)
# the next permutation consist of 2 major parts 
# 1st part : identify points of permutation [i],[j]
# loop through array in reverse order to find : 
#               nums[i] < nums[i+1]
#               nums[j] > nums[i]
# basic case    [1,2,3] -> [1,3,2]
# 2nd part : minimise permutation by reorder the list after the points of permutation
# the minimum order is achieved by re-arrange the order of all the element after point of permutation  
def nextPermutation(nums):
    descend_flg = False
    
    # 1st find the points of permutation i and j
    # find [i]
    i = len(nums) - 2
    while i >= 0:
        # loop through array in reverse order to find
        if nums[i] < nums[i + 1]:
            break
        else:
            i -= 1
    # special case array in descending order
    if i == -1:
        # special case flg
        descend_flg = True
    # find [j]
    # general case
    j = len(nums) - 1
    while j >= 0 and descend_flg == False:
        if nums[j] > nums[i]:
            # points of permutation 
            nums[i], nums[j] = nums[j], nums[i]
            break
        else:
            j -= 1

    # 2nd find minimise ordering of rest of the array (ascending order)
    # use two pointers 
    left = i+1
    right = len(nums)-1
    # reset pointer after each swap
    while left < right:
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        if nums[left] <= nums[right]:
            left += 1
            
    return nums


if __name__ == "__main__":
    nums=[4,3,2,1]
    print(nextPermutation(nums))
    