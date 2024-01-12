"""

33. Search in Rotated Sorted Array

<<<<<<< HEAD

=======
>>>>>>> refs/remotes/origin/main
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

<<<<<<< HEAD

=======
 
>>>>>>> refs/remotes/origin/main

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
<<<<<<< HEAD

=======
 
>>>>>>> refs/remotes/origin/main

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

<<<<<<< HEAD
"""

def search(nums,target):
    
    # initialise 
    left = 0
    right = len(nums) - 1 
    
    while left <= right:
        # calculate mid 
        mid = (left + right) // 2
        
        # update case
        # check which region target lies in
        # if target > nums[right]
        if target > nums[right]:
            if nums[mid] > nums[right]:
                right = mid - 1
            else:
                right = mid - 1
        else:
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                left = mid + 1
                
        print(nums[mid])
        # stop case 
        if nums[mid] == target:
            return mid
    return -1
=======

"""
def search(nums, target):
    # initialize left, right pointer 
    left = 0
    right = len(nums) -1 

    while left <= right:
        # calculate mid 
        mid = (left + right) // 2 
        # locate which region target is in 
        # if target in left region
        if target > nums[right]:
            # if mid in the same left region
            if nums[mid] > nums[right]:
                # perform binary search on the region
                # if nums[mid] > target 
                if nums[mid] > target:
                    right = mid - 1
                else :
                    left = mid + 1
            
            # if mid not in same region
            else :
                right = mid - 1

        # if target in right region
        else:
            # same region
            if nums[mid] < nums[right]:
                if nums[mid] > target :
                    right = mid - 1
                else:
                    left = mid + 1
            # different region
            else:
                left = mid + 1

        # stop case 
        if nums[mid] == target:
            return mid
    
    return -1 
>>>>>>> refs/remotes/origin/main

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
<<<<<<< HEAD
    print(search(nums,target))
=======
    print(search(nums, target))
>>>>>>> refs/remotes/origin/main
