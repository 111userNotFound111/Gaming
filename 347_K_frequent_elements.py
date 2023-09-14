"""

347 Top K Frequent Elements

Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.

"""
from collections import Counter, defaultdict
def topKFrequent(nums, k):
    output=defaultdict(list)
    # hash mapping dictionary 
    # {freq:[num]}
    freq=Counter(nums)
    sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    output=list(sorted_dict.keys())[:k]
    return output


    

    
    



if __name__ == "__main__":
    nums=[1,1,1,2,2,3]
    k=2
    print(topKFrequent(nums,k))