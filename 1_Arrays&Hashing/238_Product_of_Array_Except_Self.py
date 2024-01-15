"""
238 Product of Array Except Self

Given an integer array nums, return an array answer 
such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time 
and without using the division operation.

"""


def productExceptSelf(nums):
    # product = prefix product * surfix product

    # prefix dictionary
    # struct {position i: prefix product} 
    prefix_dict={}
    
    # initialize postfix product value 
    postfix_product=1
    
    # output list = postfix * prefix  
    output=[0] * len(nums)
    
    # for prefix
    for i in range(0,len(nums)):
        prefix_pos=i-1
        # prefix for first item
        if prefix_pos < 0:
            prefix_dict[0] = 1
        else:
            # initialize the prefix value of first item = 1 
            # prefix product [i] = prefix product[i-1] * nums[i-1] 
            prefix_dict[i]=prefix_dict[prefix_pos] * nums[prefix_pos]
        
    # for postfix
    for i in range(len(nums)-1,-1,-1):

        if i == len(nums)-1:
            postfix_product=1
        else:
            postfix_product = postfix_product * nums[i+1]
        
        #print(f'postfix_product: {postfix_product} and prefix product: {prefix_dict[i]}')
        
        output[i] = prefix_dict[i] * postfix_product
    return output

# improve efficiency, lower memory used
def productExceptSelfEfficient(nums):
    res=[1] * len(nums)
    prefix = 1 
    postfix = 1
    for i in range(0,len(nums)):
        res[i]=prefix
        prefix=prefix * nums[i]
    for j in range(len(nums)-1,-1,-1):
        res[j]=res[j]*postfix
        postfix=postfix * nums[j]
    return res

if __name__ == "__main__":
    nums = [-1,1,0,-3,3]
    print(productExceptSelfEfficient(nums))