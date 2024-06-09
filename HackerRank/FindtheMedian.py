def findMedian(arr):
    arr_sorted = sorted(arr)
    l = 0
    r = len(arr)

    if len(arr) == 0: 
        return 0
    
    median_position = (l + r) // 2
    median = arr_sorted[median_position]
    return median