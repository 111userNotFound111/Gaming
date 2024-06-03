"""
45. Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].

"""

# start from back to front 
# find leap point if exists 
# else check each jump points 
def jump(nums):
    endpoint = len(nums) - 1
    path= []
    sum = 0
    for i in range(endpoint-1,-1,-1):
        landing = i + nums[i]
        # if point reaches the end
        if landing >= endpoint:
            # check if point skips numbers 
            path.append(i)
            endpoint = i

        # check if current point skips nodes 
        # use binary search
        if landing > path[0]:
            position = path.index(landing)
            path = path[:position+1]
            path.append(i)
            endpoint = i

        # check if current point skips to the end
        if landing >= len(nums)-1:
            path = []
            path.append(i)
            endpoint = i

        print(f' i {i}  list {path}')
    return 

if __name__ == "__main__":
    nums = [4,1,1,3,1,1,1]
    jump(nums)