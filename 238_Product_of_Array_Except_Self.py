"""
238 Product of Array Except Self

Given an integer array nums, return an array answer 
such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time 
and without using the division operation.

"""
from collections import defaultdict
def productExceptSelf(nums):
    # product = prefix product * surfix product
    # prefix 
    prefix_dict={}
    # surfix 
    surfix_dict={}
    # product 
    product_dict={}

    # get prefix product for all num in list
    for index in range (0,len(nums)):
        product_list=[]
        for position in range (0, len(nums)):
            print(position)
            if position != index:
                product_list.append(nums[position])
        
        print(index)
        print(product_list)

if __name__ == "__main__":
    nums = [1,2,3,4]
    productExceptSelf(nums)