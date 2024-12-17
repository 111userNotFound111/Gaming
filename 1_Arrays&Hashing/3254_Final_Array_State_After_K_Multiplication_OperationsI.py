"""

3264 Final Array State After K Multiplication Operations I

You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
Replace the selected minimum value x with x * multiplier.
Return an integer array denoting the final state of nums after performing all k operations.


Example 1:

Input: nums = [2,1,3,5,6], k = 5, multiplier = 2

Output: [8,4,6,5,6]

Explanation:

Operation	Result
After operation 1	[2, 2, 3, 5, 6]
After operation 2	[4, 2, 3, 5, 6]
After operation 3	[4, 4, 3, 5, 6]
After operation 4	[4, 4, 6, 5, 6]
After operation 5	[8, 4, 6, 5, 6]

Example 2:

Input: nums = [1,2], k = 3, multiplier = 4

Output: [16,8]

Explanation:

Operation	Result
After operation 1	[4, 2]
After operation 2	[4, 8]
After operation 3	[16, 8]

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
1 <= k <= 10
1 <= multiplier <= 5

"""

# use a sorted list to contain the position and value
# [(1,1),(0,2),(2,3),(3,5),(4,6)]
# 


class Solution:
    def getFinalState(self, nums, k, multiplier):
        pos_dict = {}
        min = 10000
        max = 0
        for pos, num in enumerate(nums):
            if num < min:
                min = num
            if num > max:
                max = num
            pos_dict[num] = pos
        
        
        
        print(pos_dict)
        print(min, max)
        return
    
    
if __name__ == "__main__":
    test_case = [2,1,3,5,6]
    k = 5
    multiplier = 2
    solution = Solution()
    res = solution.getFinalState(test_case,k,multiplier)
    print(res)
    