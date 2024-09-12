"""

"""

import math

# find the minimum number of pages fliped to get to the target page
# begins at page 1 or the last page
# n = total number of pages
# p = target page
def pageCount(n, p):
    # declare variable 
    flipped_min = int()
    # last page
    last_page = n

    flipped_front = math.ceil((p-1)/2)

    if n % 2 != 0:
        last_page = n - 1
    flipped_back = math.ceil((last_page-p)/2)
    
    flipped_min = min(flipped_front,flipped_back)


    return flipped_min

    
if __name__ == "__main__" : 
    n = 6
    p = 3
    print(pageCount(n,p))