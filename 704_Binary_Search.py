import numpy as np
import math

def search( nums, target):
    # define new variables for left and right
    n = len(nums)
    left = 0
    right = len(nums) - 1 

    # loop stops if either left or right is greater 
    while left <= right:
        # check poisiton of the target value ( left / right )
        mid_point = left + ( (right - left ) // 2 )
        # if target is at the left side, update the mid point 
        if target < nums[mid_point] :
            right = mid_point - 1 
        elif target > nums[mid_point] :
            left = mid_point + 1 
        else :
            return print(mid_point)
        return -1 

search([1,2,3,4,5],2)