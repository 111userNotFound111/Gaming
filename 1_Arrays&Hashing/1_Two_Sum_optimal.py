nums = [3,2,4]
target = 6
def twoSum(nums, target):
        hashMap = {}
        for index, num in enumerate(nums):
                diff = target - num
                if diff in hashMap:
                    return [hashMap[diff], index]
                else:
                    hashMap[num] = index   


twoSum(nums, target)