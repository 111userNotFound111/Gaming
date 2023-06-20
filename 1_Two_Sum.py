####

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

####
nums = [3,2,4]
target = 6
def twoSum(nums, target):
        indices_list = []
        for first_index in range (0 , len(nums)-1) :
            for second_index in range (first_index+1, len(nums)):
                if nums[first_index] + nums[second_index] == target :
                    indices_list.append(first_index)
                    indices_list.append(second_index)
                    print(indices_list)
                    return indices_list

twoSum(nums, target)