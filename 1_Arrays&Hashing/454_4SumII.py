"""

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228

"""
def fourSumCount(nums1, nums2, nums3, nums4):
    # use hashing to solve
    # nums1[A] + nums2[B] + nums3[C] + nums4[D] = 0
    # nums1[A] + nums2[B] = - ( nums3[C] + nums4[D] )

    # for nums1[A] + nums2[B]
    num12_sum = {}
    for num1 in nums1:
        for num2 in nums2:
            num12_sum[num1+num2] = num12_sum.get(num1+num2, 0 ) + 1

    # for nums3[C] + nums4[D]
    count = 0
    for num3 in nums3:
        for num4 in nums4:
            count += num12_sum.get(-(num3 + num4), 0)

    return count

if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    print(fourSumCount(nums1,nums2,nums3,nums4))
