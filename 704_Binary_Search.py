"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
# def search( nums, target):
#     # define new variables for left and right
#     n = len(nums)
#     left = 0
#     right = len(nums) - 1 

#     # loop stops if either left or right is greater 
#     while left <= right:
#         # check poisiton of the target value ( left / right )
#         mid_point = left + ( (right - left ) // 2 )
#         # if target is at the left side, update the mid point 
#         if target < nums[mid_point] :
#             right = mid_point - 1 
#         elif target > nums[mid_point] :
#             left = mid_point + 1 
#         else :
#             return print(mid_point)
#         return -1 

# Binary Search
# assume : the input list is a sorted list 
# define left, right range and update condition
# define mid search condition
# locate and return target 

def search(nums, target):
    target_index = -1
    left = 0
    right = len(nums)-1
    print("start")

    while (left <= right):
        
        mid = left + ((right - left)//2)
        
        # target at the left 
        if nums[mid] > target:            
            right = mid-1
        # target at the right 
        elif nums[mid] < target:
            left = mid+1
        # nums[mid] == target
        else:
            target_index = mid
            return target_index

    # default target index -1 
    return target_index

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    print(search(nums, target))