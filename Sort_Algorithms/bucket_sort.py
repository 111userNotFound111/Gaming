# bucket sort is considered to be a rare method
# bucket sort only works if the elements of the arrays are in a finite range 
# i.e. alphabet only have 26 letters, array containing only 0,1,2 have number in finite rage of 0 to 2. 


# sort the array by bucket sort
# bucket sort uses an additional array to record frequency of each value in the array 
# the trick is how to construct the bucket list depending on the question
def bucket_sort(arr):
    if not arr:
        return arr
    
    min_val = min(arr)
    max_val = max(arr)
    
    # for this question construct bucket list based on the range of element value
    range_size = max_val - min_val + 1
    freq = [0] * range_size
    
    # element in array are sorted into bucket list based on their differences to the min_value 
    for num in arr:
        freq[num - min_val] += 1
    
    # based on bucket list, re-order the value in array
    i=0
    for value, count in enumerate(freq):
        print(value, count)
        for frequency in range(count):
            arr[i] = value + min_val
            i+= 1
            
    print(freq)
    return arr

if __name__ == "__main__":
    test_array = [1,5,5,6]
    res = bucket_sort(test_array)
    print(res)
