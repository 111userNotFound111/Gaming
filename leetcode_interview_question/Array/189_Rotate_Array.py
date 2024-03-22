"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Do not return anything, modify nums in-place instead.

"""

def rotate(nums, k):
    # if length of array greater than k 
    if len(nums) > k:
        rotate_position = len(nums)-k
    elif len(nums) == k:
        return nums
    # if length of array smaller than k
    # use mod to determine the new k value 
    else:
        new_k = k % len(nums)
        rotate_position = len(nums) - new_k
    
    # slice the list and recombined the new list in place of nums
    sliced_list = nums[rotate_position:]
    original = nums[:rotate_position]
    # modifies nums in-place
    nums[:] = sliced_list + original
    return


if __name__ == "__main__":
    nums = [1,2]
    k = 3
    rotate(nums, k)