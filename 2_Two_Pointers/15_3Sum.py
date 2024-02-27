
def threeSum(nums):
    
        # two pointer questions generally requires the list to be sorted first 
        nums.sort()
        result = []
        for index, num in enumerate(nums):
            print(index)
            if index != 0 and num == nums[index - 1]: # if the current value is the same as previous value in the array
                continue
            
            left = index + 1 
            right = len(nums) - 1 
            
            while left < right:
                sum = num + nums[left] + nums[right]
                
                if sum < 0 :
                    left = left + 1
                if sum > 0 :
                    right = right - 1 
                else : 
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
        return result
    
if __name__ == "__main__":
    nums = [1,2,3,4,5]
    threeSum(nums)