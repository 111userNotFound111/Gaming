"""
217 Contains Duplicate:

Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.

"""
from collections import Counter

# hashmapping method
def detect_duplicate(nums):
    # remember scanned values 
    hash_set=set()
    # scan input list 
    for num in nums:
        if num in hash_set:
            return True
        hash_set.add(num)
        #print(scanned_list)
    return False

# check for adjcent values 
def two_pointer_detect(nums):
    # first sort the list
    nums_sorted = sorted(nums)
    # use two pointers to find at least twice 
    for i in range(0,len(nums_sorted)-1):
        print(i)
        if nums_sorted[i] == nums_sorted[i+1]:
            return True
    return False

# use collection.counter() method
def counting_duplicate(nums):
    freq_dict=Counter(nums)
    print(freq_dict.values())
    for freq in freq_dict.values():
        if freq != 1:
            return True
    return False


if __name__ == "__main__":
    list = [1,2,3,3]
    print(counting_duplicate(list))