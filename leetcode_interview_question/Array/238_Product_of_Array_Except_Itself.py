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

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


"""

# structure 
# 1. prefix product : product of all numbers before the current num (left of the curr num)
# 2. suffix product : product of all numbers after teh current num(right of the curr num)
# 3. multiple products : left product x right product 
class Solution:
    def productExceptSelf(self, nums):
        prefix_product = []
        suffix_product = [1]* len(nums)
        multiple_product = []
        # 1. prefix product 
        for index in range(len(nums)):
            if index == 0:
                current_multiple = 1 * nums[index]
            else:
                current_multiple = prefix_product[-1] * nums[index]
            prefix_product.append(current_multiple)
        
        # 2. suffix product
        for index in range(len(nums)-1,-1,-1):
            if index == len(nums)-1:
                current_multiple = 1 * nums[index]
            else:
                current_multiple = suffix_product[index+1] * nums[index]
            suffix_product[index] = current_multiple
        
        # 3. multiple products 
        for index in range(len(nums)):
            if index == 0:
                current_multiple_product = 1 * suffix_product[index+1]
            elif index + 1 == len(nums):
                current_multiple_product = prefix_product[index-1] * 1
            else:
                current_multiple_product = prefix_product[index-1] * suffix_product[index+1]
            
            multiple_product.append(current_multiple_product)
            
        # return product except itself
        return multiple_product
            


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4]
    result = solution.productExceptSelf(nums)
    print(result)