"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109

"""

def two_sum(nums,target):
    remainder_dict={}
    for index, value in enumerate(nums):
        remainder=target - value
        if remainder in remainder_dict.keys():
            output=[remainder_dict[remainder],index]
            return output
        else:
            remainder_dict[value] = index

if __name__ == "__main__":
    nums = [3,3]
    target = 6
    print(two_sum(nums,target))