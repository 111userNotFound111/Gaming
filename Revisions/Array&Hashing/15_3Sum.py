def threeSum(nums):
    nums = sorted(nums)
    ans = []
    for index, num in enumerate(nums):
        print("current index",index)
        print("program starts")
        # no duplicate triplets 
        if index != 0 and nums[index] == nums[index-1]:
            continue
        
        # ask for 3 sums, when index moved to second last element, return the ans
        if index == len(nums) - 2:
            break
        
        left = index + 1 
        right = len(nums) - 1 
        
        while left < right:
            sum = num + nums[left] + nums[right]
            if sum < 0 :
                left = left + 1 
            if sum > 0 :
                right = right - 1 
            if sum == 0:
                ans.append([num, nums[left], nums[right]])
                left = left + 1 
                # check the new 
                while nums[left] == nums[left - 1] and left < right:
                    left += 1 
        
    return ans

if __name__ == "__main__":
    nums = [0,0,0]
    print(threeSum(nums))
    