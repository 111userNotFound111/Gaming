"""
11. Container With Most Water

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

"""


#Two pointer method 

# pointer update condition 

# most_water = max(cur_water, most_water)

def maxArea(height):
    #define left and right pointer 
    left = 0
    right = len(height)-1
    max_water = 0

    # looping condiction
    # left == right is point less as height is [left, right)
    while (left < right):
        # water = height * distance
        cur_water = min(height[left], height[right]) * (right - left)
        print(f'left : {left}, right {right}, {cur_water}')
        max_water = max(cur_water, max_water)

        # 3 condictions 
        # 1. left is small
        # 2. right is small
        # 3. both the same value 
        if min(height[left], height[right]) == height[left]:
            left += 1
        elif min(height[left], height[right]) == height[right]:
            right -= 1
        else:
            left += 1
            right -= 1

    return max_water


if __name__ == "__main__":
    height= [1,1]
    print(maxArea(height))