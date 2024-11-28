"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

"""


# for constant extra space O(1)
# use Floyd's cycle detection algorithm (slow fast pointer)
# 1. identify the question as linkedlist question 
# 2. apply Floyd's cycle detection, the head of the cycle is the duplicate value
class Solution:
    def findDuplicate(self, nums):
        # Initialise Floyd's slow fast pointer 
        slow = nums[0]
        fast = nums[0]

        # part 1: find the cycle in linkedlist 
        while True:
            # slow jumps 1 node
            # fast jumps 2 nodes 
            slow = nums[slow]
            fast = nums[nums[fast]]
            # the slow and fast pointer will always meet in the cycle, 
            # but the intersection might not be the entry point (duplicate) of the cycle
            if slow == fast:
                break
        
        # part 2 : find the entry point of the cycle (duplicate number)
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow
        return 


if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,4,2,2]
    output = solution.findDuplicate(nums)
    print(output)