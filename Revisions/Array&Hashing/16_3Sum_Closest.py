"""
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

"""

def threeSumClosest(nums,target):
    # sort nums in ascending order
    nums = sorted(nums)
    # initialise variable to store closest value 
    closest_sum = sum(nums[:3])
    # use flg to signal breaking of the nested loop
    flg_stop = False
    # boundary conditions 
    if len(nums) == 3:
        return sum(nums)
    
    for index , num in enumerate(nums):
        left = index + 1 
        right = len(nums) - 1
        # use two pointer operation 
        while left < right:
            three_sum = num + nums[left] + nums[right]
            
            if abs(three_sum - target) < abs(closest_sum - target):
                closest_sum = three_sum
            
            if three_sum < target: 
                left += 1
            elif three_sum > target:
                right -= 1
            else:
                return three_sum

    return closest_sum

if __name__ == "__main__":
    nums = [1,1,1,1]
    target = 3
    print(threeSumClosest(nums,target))