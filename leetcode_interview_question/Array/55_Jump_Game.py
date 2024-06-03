"""
55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.


Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

"""

# def canJump(nums):

#     total_len = len(nums)
#     start_position = 0

#     def recursive_jump(nums, start_position, total_len):
#         print(f'recursion starts    current position {start_position}')
#         # check the current jump distance
#         jump_dist = nums[start_position]
#         land_index_max = start_position + jump_dist
#         print(f'land position max {land_index_max}')

#         # stop case 1: if jumped till the end return true
#         if land_index_max > total_len:
#             return True
#         # stop case 2: if no more jumps and not at end return false (stucked)
#         if jump_dist == 0:
#             print('dead end')
#             return False
        
#         # update case
#         if start_position < total_len:
#             # greedy algo
#             for jump in range(land_index_max,start_position,-1):
#                 jump_outcome = recursive_jump(nums, jump, total_len)
#                 if jump_outcome == True:
#                     return True
#                 else:
#                     continue
#             return False

#     # execute the function 
#     outcome = recursive_jump(nums, start_position, total_len)
#     if outcome == True:
#         return True
#     else:
#         return False

def canJump(nums):
    gas = 0
    for n in nums:
        print(gas, n)
        # for case [0], where it should output true
        if gas < 0:
            return False
        elif n > gas:
            gas = n
        gas -= 1
    return True
    
if __name__ == "__main__":
    nums = [0]
    print(canJump(nums))