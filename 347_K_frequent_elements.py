"""

347 Top K Frequent Elements

Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.

"""
# use collections and Counter
from collections import Counter, defaultdict
def topKFrequent(nums, k):
    output=defaultdict(list)
    # hash mapping dictionary 
    # {freq:[num]}
    freq=Counter(nums)
    sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    output=list(sorted_dict.keys())[:k]
    return output

# use hash mapping (bucket sort algorithm)
def topKFrequentHash(nums,k):
    # initialize dict for counting frequency
    count={}
    # initialize bucket for bucket sort 
    freq=[[] for i in range(len(nums)+1)]
    print(freq)
    # initialize list to store result
    res=[]

    for n in nums:
        # .get() method in dictionary 
        # get number of n stored in dictionary
        # if n is not present in dictionary, return 0
        # this line search for key n in dictionary "count"
        # and update the value 
        count[n] = 1 + count.get(n,0)
    
    # 
    for n, c in count.items():
        freq[c].append(n)

    #print(freq)
    #print(count)

    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

if __name__ == "__main__":
    nums=[4,1,-1,2,-1,2,3]
    k=2
    #print(topKFrequent(nums,k))
    print(topKFrequentHash(nums,k))