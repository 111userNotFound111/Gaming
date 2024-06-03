"""

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""

# use divide and conquer technique 
class Solution:
    def productExceptSelf(self, nums):
        # construct left and right table 
        left = [0] * len(nums)
        right = [0] * len(nums)
        # for left list : the product of number to the left of num[i]
        left[0] = 1
        for i in range(1,len(nums)):
            left[i] = nums[i-1] * left[i-1]
        
        # for right list : the product of number to the right of num[i]
        right[len(nums)-1] = 1
        for i in range(len(nums)-2,-1,-1):
            right[i] = nums[i+1] * right[i+1]
            
        # product = product_left * product_right
        res = [0] * len(nums)
        for i in range(0,len(nums)):
            res[i] = left[i] * right[i]
        return res



if __name__ == "__main__":
    nums = [1,2,3,4]
    solution = Solution()
    product = solution.productExceptSelf(nums)