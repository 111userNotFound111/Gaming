"""

128. Longest Consecutive Sequence

Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

"""

from collections import defaultdict
    

# return the length of current sequence 
def recursiveFind(num_set,cur_num,seq_length):

    # update
    next_num = cur_num + 1
    new_seq_length = seq_length + 1

    # stop case 
    if next_num not in num_set:
        return new_seq_length
    
    # recursive case 
    else:
        return recursiveFind(num_set, next_num, new_seq_length)

   

def longestConsecutive(nums):
    longest_length=0
    num_set = set(nums)
    # find start of sequence 
    # check if left num exists:
    # if left num exist, it's not a start of sequence 
    for num in num_set:
        left_num=num-1
        # if not exist in set, its a start of sequence 
        if left_num not in num_set :
            length=0

            while (num + length) in num_set:
                length += 1

            # check if its longest length
            if length > longest_length:
                longest_length = length
    
            
    
    return longest_length
            


if __name__ == "__main__":
    nums = [10,9,8,7,6,5,4,3,2,1,0]
    print(1)
    print(longestConsecutive(nums))