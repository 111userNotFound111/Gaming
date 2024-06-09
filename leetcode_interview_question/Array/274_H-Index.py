"""

274. H-Index

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.


Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1


Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""

class Solution:
    # hindex : at least h number of citations for h number of published papers
    def hIndex(self, citations):
        # In terms of citations 
        # 1. sorted citations list 
        # 2. loop through citations list 
        # 3. calculate remaining papers  = len(list) - pos
        # 4. compare with current citation value 
        # 5. index is the minimum of remaining paper or citation 
        # 6. find the largest index as the hIndex 
        hindex = 0
        list_len = len(citations)
        citations_sorted = sorted(citations)
        for position, citation in enumerate(citations_sorted):
            remaining = list_len - position
            index = min(remaining, citation)
            if index >= hindex:
                hindex = index
            else:
                break
            
        return hindex
    
    def hIndex_better(self, citations):
        # in terms of positions
        # hIndex = position that is smaller or equal to citations
        hIndex = 0
        list_len = len(citations)
        citations = sorted(citations)
        print(citations)
        for position, citation in enumerate(citations):
            if list_len - position <= int(citation):
                hIndex = list_len - position
                return hIndex
        return hIndex
    
if __name__ == "__main__":
    solution = Solution()
    citations = [3,0,6,1,5]
    res = solution.hIndex(citations)
    print(res)