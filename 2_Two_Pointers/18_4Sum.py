"""

18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

"""

def fourSum(nums, target):
    nums = sorted(nums)
    print(nums)
    res = []

    if len(nums) < 4:
        return res

    for i, num in enumerate(nums):
        if i > len(nums) - 3:
            break
        # can not have duplicate values for first position again
        if i > 0 and nums[i] == nums[i-1]:
            continue

        for j in range (i+1, len(nums)-2):
            # can not have duplicate values for second position again
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            left = j + 1 
            right = len(nums) - 1 
            while left < right:
                four_sum = num + nums[j] + nums[left] + nums[right]
                if four_sum < target :
                    left += 1
                if four_sum > target :
                    right -= 1
                if four_sum == target :
                    res.append([nums[i],nums[j],nums[left],nums[right]])
                    # update pointers 
                    left += 1
                    right -= 1
                    # check new position contains no duplicate for third and fourth number
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
    return res

if __name__ == "__main__":
    print("hello")
    nums = [-2,-1,-1,1,1,2,2]
    target = 0
    print(fourSum(nums, target))