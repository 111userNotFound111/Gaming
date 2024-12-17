"""
    sort array in place using quick sort 
    
    input: [6,2,4,1,3]
    output: [1,2,3,4,6]
    
"""

# quick sort
# array in place sorting with
# Time efficiency :  best: O(nlogn)  worst: O(n^2)
def quick_sort(arr, low=0, high=None):
    
    # low : pointing at lower boundary of the array
    # high pointer : pointing at upper boundary of the array (also assume the upper bound is the pivot)
    # left : pointer pointing at the last swapping position (dividing array into left and right)
    
    # initialise first high pointer
    if high == None:
        high = len(arr) - 1
    # initialise left pointer 
    left = low
    # base case: if both pointers are at the same position, return 
    if low >= high:
        return arr
    
    for i in range (low, high):
        if arr[i] < arr[high]:
            temp = arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            left += 1
    
    # swap pivot value with the last insertion position 
    # reason : we assume that pivot value is the middle number of the array
    #          under this assumption there are maximum n/2 times of swaps and last swapping position is at the middle of the array
    #          perfect case : [1,2,4,5,3]
    temp = arr[left]
    arr[left] = arr[high]
    arr[high] = temp
    
        
    print(f'the current array:{arr}, the lower bound:{low}, the upper bound:{high}, last point of swap:{left}')
    
    # excluding the pivot value, divide array into left and right sub arrays
    quick_sort(arr, low , left-1)
    quick_sort(arr, left+1, high)
    
    return arr



if __name__ == "__main__":
    test_case = [1,6,3,2,4]
    res = quick_sort(test_case)
    # print(res)