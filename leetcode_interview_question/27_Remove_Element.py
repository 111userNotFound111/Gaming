"""

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100


"""

# def removeElement(nums:list,val):
#     left = 0
#     right = len(nums)-1
    
#     while left <= right:
#         if nums[left] == val:
#             if nums[right] == val:
#                 nums[right] = "_"
#                 nums.pop(left)
#                 nums.append('_')
#                 right -= 2
#             else:
#                 nums[left] = nums[right]
#                 nums[right] = "_"
#                 left += 1
#                 right -= 1
#         else:
#             if nums[right] == val:
#                 nums[right] = "_"
#                 right -= 1
                
#             left += 1
    
#     count = 0
#     while count < len(nums):
#         if nums[count] == "_":
#             break
#         else:
#             count += 1
    
#     return count, nums


# def removeElement(nums:list,val):
#     left = 0
#     right = len(nums)-1
#     count = len(nums)
    
#     while left <= right:
#         if left == right:
#             if nums[left] == val:
#                 nums.pop(left)
#                 count -= 1
#                 break
            
#         if nums[left] == val:
#             if nums[right] == val:
#                 nums.pop(right-1)
#                 nums.pop(left)
#                 right -= 2
#                 count -= 2
#             else:
#                 nums[left] = nums[right]
#                 left += 1
#                 nums.pop(right)
#                 right -= 1
#                 count -= 1
#         else:
#             if nums[right] == val:
#                 nums.pop(right)
#                 right -= 1
#                 count -= 1
#             left += 1

#     return count, nums


def removeElement(nums:list,val):
    res = []
    left = 0
    right = len(nums)-1
    
    while left < right:
        if nums[left] != val:
            res.append(nums[left])
        if nums[right] != val:
            res.append(nums[right])
        left+=1
        right-=1
    
    if left == right:
        if nums[left] != val:
            res.append(nums[left])
    
    for i in range (0, len(res)):
        nums[i] = res[i]
        
    return len(res)

if __name__ == "__main__":
    nums = [2,2,2]
    val = 0
    print(removeElement(nums,val))